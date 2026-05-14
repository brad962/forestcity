#!/usr/bin/env python3
"""
Slack Photo Watcher
Polls #fc-requests for new image uploads.
- 1st new photo in a batch = "before"
- 2nd new photo in a batch = "after"
Saves as before_[date]_[name].jpg and after_[date]_[name].jpg
Writes completed pairs to logs/photo_pairs.json for Jasmine to pick up.
Pushes to GitHub and confirms in Slack.
Run via cron every 5 minutes.
"""

import json
import os
import subprocess
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path

BASE_DIR   = Path(__file__).parent.parent.resolve()
PHOTOS_DIR = BASE_DIR / 'assets' / 'photos'
SEEN_FILE  = BASE_DIR / 'logs' / 'seen_photos.json'
PAIRS_FILE = BASE_DIR / 'logs' / 'photo_pairs.json'
LOG_FILE   = BASE_DIR / 'logs' / 'activity.log'


def _load_env():
    env_file = BASE_DIR / '.env'
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                os.environ.setdefault(k.strip(), v.strip())


_load_env()

SLACK_TOKEN   = os.environ.get('SLACK_TOKEN', '')
CHANNEL_ID    = 'C0B3FR6Q0PP'
SLACK_WEBHOOK = os.environ.get('SLACK_WEBHOOK_OFFICE', '')
GITHUB_PAT    = os.environ.get('GITHUB_PAT', '')
GITHUB_RAW    = 'https://raw.githubusercontent.com/brad962/forestcity/main'

IMAGE_TYPES = {'jpg', 'jpeg', 'png', 'gif', 'webp', 'heic', 'heif'}


# ── Seen file ──

def load_seen():
    if not SEEN_FILE.exists():
        return set(), None
    data = json.loads(SEEN_FILE.read_text())
    if isinstance(data, list):
        return set(data), None
    return set(data.get('seen', [])), data.get('pending_before')


def save_seen(seen, pending_before=None):
    SEEN_FILE.parent.mkdir(exist_ok=True)
    data = {'seen': list(seen)}
    if pending_before:
        data['pending_before'] = pending_before
    SEEN_FILE.write_text(json.dumps(data, indent=2))


# ── Photo pairs file ──

def load_pairs():
    if not PAIRS_FILE.exists():
        return {'pairs': []}
    return json.loads(PAIRS_FILE.read_text())


def record_pair(before_rel, after_rel, description=''):
    pairs = load_pairs()
    # Dedup — don't create a pair if this before+after combo already exists
    for existing in pairs['pairs']:
        if existing.get('before') == before_rel and existing.get('after') == after_rel:
            print(f'Pair already exists for {before_rel} + {after_rel}, skipping.')
            return existing['id']
    pair = {
        'id': f'pair_{datetime.now().strftime("%Y%m%d_%H%M%S")}',
        'before': before_rel,
        'after': after_rel,
        'date': datetime.now().strftime('%Y-%m-%d'),
        'description': description,
        'processed': False,
    }
    pairs['pairs'].append(pair)
    PAIRS_FILE.write_text(json.dumps(pairs, indent=2))
    return pair['id']


# ── Slack helpers ──

def slack_get(endpoint, params=''):
    url = f'https://slack.com/api/{endpoint}?{params}'
    req = urllib.request.Request(url, headers={'Authorization': f'Bearer {SLACK_TOKEN}'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read())


def notify_slack(msg, webhook=None):
    target = webhook or SLACK_WEBHOOK
    try:
        payload = json.dumps({'text': msg}).encode()
        req = urllib.request.Request(target, data=payload, headers={'Content-Type': 'application/json'})
        urllib.request.urlopen(req, timeout=5)
    except Exception:
        pass


def download_file(url, dest_path):
    req = urllib.request.Request(url, headers={'Authorization': f'Bearer {SLACK_TOKEN}'})
    with urllib.request.urlopen(req, timeout=30) as resp:
        dest_path.write_bytes(resp.read())


def log(msg):
    ts = datetime.now().strftime('%Y-%m-%d %H:%M')
    LOG_FILE.parent.mkdir(exist_ok=True)
    with open(LOG_FILE, 'a') as f:
        f.write(f'[{ts}] Office | Slack photo watcher | {msg} | Done\n')


def git_push(files_added):
    try:
        subprocess.run(['git', '-C', str(BASE_DIR), 'add'] + [str(f) for f in files_added], capture_output=True)
        subprocess.run(['git', '-C', str(BASE_DIR), 'config', 'user.email', 'office@forestcitypowerwashing.com'], capture_output=True)
        subprocess.run(['git', '-C', str(BASE_DIR), 'config', 'user.name', 'Forest City AI Office'], capture_output=True)
        subprocess.run(['git', '-C', str(BASE_DIR), 'commit', '-m', f'Photos added from Slack {datetime.now().strftime("%Y-%m-%d")}'], capture_output=True)
        subprocess.run(['git', '-C', str(BASE_DIR), 'remote', 'set-url', 'origin',
                        f'https://{GITHUB_PAT}@github.com/brad962/forestcity.git'], capture_output=True)
        subprocess.run(['git', '-C', str(BASE_DIR), 'push', 'origin', 'main'], capture_output=True, timeout=15)
    except Exception as e:
        print(f'Git push failed: {e}')


def run():
    PHOTOS_DIR.mkdir(parents=True, exist_ok=True)
    seen, pending_before = load_seen()

    data = slack_get('conversations.history', f'channel={CHANNEL_ID}&limit=50')
    if not data.get('ok'):
        print(f'Slack API error: {data.get("error")}')
        return

    messages = list(reversed(data.get('messages', [])))  # oldest first
    new_photos = []
    new_pairs  = []

    for msg in messages:
        # Grab any text description from the message (used for Facebook post)
        msg_text = msg.get('text', '').strip()

        files = msg.get('files', [])
        # Filter to unseen images only
        new_images = []
        for f in files:
            file_id  = f.get('id', '')
            filetype = f.get('filetype', '').lower()
            filename = f.get('name', f'{file_id}.jpg')
            if file_id in seen:
                continue
            if filetype not in IMAGE_TYPES and not any(filename.lower().endswith(ext) for ext in IMAGE_TYPES):
                continue
            dl_url = f.get('url_private_download') or f.get('url_private', '')
            if not dl_url:
                continue
            new_images.append((file_id, filename, dl_url))

        # If message has 2+ new images, treat as before+after in one shot
        if len(new_images) >= 2 and pending_before is None:
            date_str = datetime.now().strftime('%Y-%m-%d')
            downloaded = []
            for file_id, filename, dl_url in new_images[:2]:
                prefix    = 'before' if not downloaded else 'after'
                safe_name = filename.replace(' ', '_')
                dest      = PHOTOS_DIR / f'{prefix}_{date_str}_{safe_name}'
                try:
                    download_file(dl_url, dest)
                    seen.add(file_id)
                    new_photos.append(dest)
                    downloaded.append(dest)
                    print(f'Downloaded ({prefix}): {dest.name}')
                except Exception as e:
                    print(f'Failed to download {filename}: {e}')
            if len(downloaded) == 2:
                before_rel = str(downloaded[0].relative_to(BASE_DIR))
                after_rel  = str(downloaded[1].relative_to(BASE_DIR))
                pair_id    = record_pair(before_rel, after_rel, msg_text)
                new_pairs.append((before_rel, after_rel, pair_id))
                print(f'Pair complete (same message): {pair_id} | description: "{msg_text[:60]}"')
            continue

        # Otherwise process one at a time (before from one message, after from next)
        for file_id, filename, dl_url in new_images:
            date_str  = datetime.now().strftime('%Y-%m-%d')
            safe_name = filename.replace(' ', '_')
            prefix    = 'before' if pending_before is None else 'after'
            dest      = PHOTOS_DIR / f'{prefix}_{date_str}_{safe_name}'

            try:
                download_file(dl_url, dest)
                seen.add(file_id)
                new_photos.append(dest)
                print(f'Downloaded ({prefix}): {dest.name}')

                if pending_before is None:
                    pending_before = {
                        'file_id': file_id,
                        'path': str(dest.relative_to(BASE_DIR)),
                        'description': msg_text,
                    }
                else:
                    after_rel   = str(dest.relative_to(BASE_DIR))
                    before_rel  = pending_before['path']
                    description = msg_text or pending_before.get('description', '')
                    pair_id     = record_pair(before_rel, after_rel, description)
                    new_pairs.append((before_rel, after_rel, pair_id))
                    print(f'Pair complete: {pair_id} | description: "{description[:60]}"')
                    pending_before = None

            except Exception as e:
                print(f'Failed to download {filename}: {e}')

    if new_photos:
        files_to_push = new_photos + [SEEN_FILE]
        if new_pairs:
            files_to_push.append(PAIRS_FILE)

        git_push(files_to_push)
        save_seen(seen, pending_before)
        log(f'{len(new_photos)} photo(s) saved — {len(new_pairs)} pair(s) ready for Jasmine')

        if new_pairs:
            pair_summary = '\n'.join(
                f'  • {p[0].split("/")[-1]} + {p[1].split("/")[-1]}'
                for p in new_pairs
            )
            notify_slack(
                f'📸 *New before/after pair ready for Jasmine*\n{pair_summary}\nJasmine will generate the Canva flyer within the hour.'
            )
        else:
            notify_slack(
                "📷 Before photo saved. Drop the 'after' shot whenever it's ready and Jasmine will build the flyer."
            )

        print(f'Done — {len(new_photos)} photo(s), {len(new_pairs)} pair(s) queued.')
    else:
        save_seen(seen, pending_before)
        print('No new photos found.')


if __name__ == '__main__':
    run()
