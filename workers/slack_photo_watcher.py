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

BASE_DIR      = Path(__file__).parent.parent.resolve()
PHOTOS_DIR    = BASE_DIR / 'assets' / 'photos'
SEEN_FILE     = BASE_DIR / 'logs' / 'seen_photos.json'
PAIRS_FILE    = BASE_DIR / 'logs' / 'photo_pairs.json'
LOG_FILE      = BASE_DIR / 'logs' / 'activity.log'

SLACK_TOKEN   = 'xoxb-6370405798291-11119187295830-usQPETKIgHmPwRYAW9QRAxi7'
CHANNEL_ID    = 'C0B3FR6Q0PP'
SLACK_WEBHOOK = 'https://hooks.slack.com/services/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'
GITHUB_PAT    = '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'
GITHUB_RAW    = 'https://raw.githubusercontent.com/brad962/forestcity/main'

IMAGE_TYPES = {'jpg', 'jpeg', 'png', 'gif', 'webp', 'heic', 'heif'}


# ── Seen file (tracks seen IDs + any pending "before" waiting for its "after") ──

def load_seen():
    if not SEEN_FILE.exists():
        return set(), None
    data = json.loads(SEEN_FILE.read_text())
    # Migrate old flat-list format
    if isinstance(data, list):
        return set(data), None
    return set(data.get('seen', [])), data.get('pending_before')


def save_seen(seen, pending_before=None):
    SEEN_FILE.parent.mkdir(exist_ok=True)
    data = {'seen': list(seen)}
    if pending_before:
        data['pending_before'] = pending_before
    SEEN_FILE.write_text(json.dumps(data, indent=2))


# ── Photo pairs file (Jasmine reads this to know what to design) ──

def load_pairs():
    if not PAIRS_FILE.exists():
        return {'pairs': []}
    return json.loads(PAIRS_FILE.read_text())


def record_pair(before_rel, after_rel):
    pairs = load_pairs()
    pair = {
        'id': f'pair_{datetime.now().strftime("%Y%m%d_%H%M%S")}',
        'before': before_rel,
        'after': after_rel,
        'date': datetime.now().strftime('%Y-%m-%d'),
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

    # Pull last 50 messages from #fc-requests, process oldest-first so
    # the chronological upload order (before → after) is preserved.
    data = slack_get('conversations.history', f'channel={CHANNEL_ID}&limit=50')
    if not data.get('ok'):
        print(f'Slack API error: {data.get("error")}')
        return

    messages = list(reversed(data.get('messages', [])))  # oldest first
    new_photos   = []
    new_pairs    = []

    for msg in messages:
        files = msg.get('files', [])
        for f in files:
            file_id  = f.get('id', '')
            filetype = f.get('filetype', '').lower()
            filename = f.get('name', f'{file_id}.jpg')

            if file_id in seen:
                continue
            if filetype not in IMAGE_TYPES and not any(filename.lower().endswith(ext) for ext in IMAGE_TYPES):
                continue

            date_str  = datetime.now().strftime('%Y-%m-%d')
            safe_name = filename.replace(' ', '_')

            # 1st new photo = "before", 2nd = "after"
            if pending_before is None:
                prefix = 'before'
            else:
                prefix = 'after'

            dest = PHOTOS_DIR / f'{prefix}_{date_str}_{safe_name}'

            dl_url = f.get('url_private_download') or f.get('url_private', '')
            if not dl_url:
                continue

            try:
                download_file(dl_url, dest)
                seen.add(file_id)
                new_photos.append(dest)
                print(f'Downloaded ({prefix}): {dest.name}')

                if pending_before is None:
                    # Store this as the pending "before"
                    pending_before = {
                        'file_id': file_id,
                        'path': str(dest.relative_to(BASE_DIR)),
                    }
                else:
                    # We have a complete pair — record it
                    after_rel  = str(dest.relative_to(BASE_DIR))
                    before_rel = pending_before['path']
                    pair_id    = record_pair(before_rel, after_rel)
                    new_pairs.append((before_rel, after_rel, pair_id))
                    print(f'Pair complete: {pair_id}')
                    pending_before = None  # reset for next pair

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
            # Tell #fc-ai-office that Jasmine has new material to work with
            pair_summary = '\n'.join(
                f'  • {p[0].split("/")[-1]} + {p[1].split("/")[-1]}'
                for p in new_pairs
            )
            notify_slack(
                f'📸 *New before/after pair ready for Jasmine*\n{pair_summary}\nJasmine will generate the Canva flyer shortly.'
            )
            # Confirm in #fc-requests
            notify_slack(
                f'Got it! Before & after saved. Jasmine will turn these into a flyer and post it to #fc-ai-office.',
                webhook=None  # reuse main webhook — swap if you have a separate fc-requests webhook
            )
        else:
            # Just a before photo, waiting on the after
            notify_slack(
                f'📷 Before photo saved. Drop the "after" shot whenever it\'s ready and Jasmine will build the flyer.',
            )

        print(f'Done — {len(new_photos)} photo(s) saved, {len(new_pairs)} pair(s) queued.')
    else:
        save_seen(seen, pending_before)
        print('No new photos found.')


if __name__ == '__main__':
    run()
