#!/usr/bin/env python3
"""
Vera Relay — runs locally every 5 minutes.
Pulls latest commits from GitHub, checks for new Vera Cole pushes,
reads pending_slack_messages.md, posts each message to Slack, then clears the file.
"""

import json
import os
import subprocess
import urllib.request
from datetime import datetime
from pathlib import Path
import time

BASE_DIR = Path(__file__).parent.parent.resolve()
PENDING_FILE = BASE_DIR / 'outputs' / 'vera' / 'pending_slack_messages.md'
STATE_FILE = BASE_DIR / 'outputs' / 'vera' / 'relay_last_commit.txt'
LOG_FILE = BASE_DIR / 'logs' / 'activity.log'
LOCK_FILE = BASE_DIR / 'outputs' / 'vera' / '.relay_lock'
LOCK_TIMEOUT_SECONDS = 180  # if lock is older than 3 min, assume stale and override

# Load env
_env = BASE_DIR / '.env'
if _env.exists():
    for line in _env.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith('#') and '=' in line:
            k, v = line.split('=', 1)
            os.environ.setdefault(k.strip(), v.strip())

SLACK_WEBHOOK = os.environ.get('SLACK_WEBHOOK_OFFICE', '')


def log(msg):
    ts = datetime.now().strftime('%Y-%m-%d %H:%M')
    LOG_FILE.parent.mkdir(exist_ok=True)
    with open(LOG_FILE, 'a') as f:
        f.write(f'[{ts}] Vera Relay | {msg}\n')


def post_slack(msg):
    if not SLACK_WEBHOOK:
        print('No Slack webhook configured')
        return False
    try:
        payload = json.dumps({'text': msg}).encode()
        req = urllib.request.Request(
            SLACK_WEBHOOK, payload,
            {'Content-Type': 'application/json'}
        )
        urllib.request.urlopen(req, timeout=10)
        return True
    except Exception as e:
        print(f'Slack post failed: {e}')
        return False


def git(cmd):
    return subprocess.run(
        ['git', '-C', str(BASE_DIR)] + cmd,
        capture_output=True, text=True
    )


def _check_danny_staleness():
    """Check when Danny last ran. Post Slack alert if > 7 days. Once per day."""
    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.danny_alert_sent_date'
    pull_sentinel  = BASE_DIR / 'outputs' / 'vera' / '.danny_last_pull_date'
    today_str = datetime.now().strftime('%Y-%m-%d')

    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return  # Already alerted today

    last_pull_dt = None
    # Use sentinel file first (written by lead_pipeline.py — more reliable than log parsing)
    if pull_sentinel.exists():
        try:
            last_pull_dt = datetime.strptime(pull_sentinel.read_text().strip(), '%Y-%m-%d')
        except Exception:
            pass
    # Fall back to log parsing if sentinel not found
    if last_pull_dt is None and LOG_FILE.exists():
        try:
            for line in reversed(LOG_FILE.read_text().splitlines()):
                if 'Danny' in line and 'Apollo pull' in line:
                    date_part = line[1:11]
                    last_pull_dt = datetime.strptime(date_part, '%Y-%m-%d')
                    break
        except Exception:
            pass

    days_stale = (datetime.now() - last_pull_dt).days if last_pull_dt else 99
    if days_stale < 7:
        return

    label = last_pull_dt.strftime('%B %d') if last_pull_dt else 'unknown'
    msg = (
        f'🔴 *Danny Cron Alert — {days_stale} days since last lead pull*\n'
        f'>Last pull: {label}\n'
        f'>Run NOW: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py danny`\n'
        f'>Round 2 enrollment June 4 — needs Summit + Medina leads before June 2.'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Danny staleness alert posted — {days_stale} days since last pull')


def _check_carla_staleness():
    """Check when Carla last ran. Post Slack alert if > 10 days. Once per day."""
    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.carla_alert_sent_date'
    pull_sentinel  = BASE_DIR / 'outputs' / 'vera' / '.carla_last_pull_date'
    today_str = datetime.now().strftime('%Y-%m-%d')

    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    last_pull_dt = None
    # Use sentinel file first (written by lead_pipeline.py — more reliable than log parsing)
    if pull_sentinel.exists():
        try:
            last_pull_dt = datetime.strptime(pull_sentinel.read_text().strip(), '%Y-%m-%d')
        except Exception:
            pass
    # Fall back to log parsing if sentinel not found
    if last_pull_dt is None and LOG_FILE.exists():
        try:
            for line in reversed(LOG_FILE.read_text().splitlines()):
                if 'Carla' in line and 'Apollo pull' in line:
                    date_part = line[1:11]
                    last_pull_dt = datetime.strptime(date_part, '%Y-%m-%d')
                    break
        except Exception:
            pass

    days_stale = (datetime.now() - last_pull_dt).days if last_pull_dt else 99
    if days_stale < 10:
        return

    label = last_pull_dt.strftime('%B %d') if last_pull_dt else 'unknown'
    msg = (
        f'🟣 *Carla Cron Alert — {days_stale} days since last referral partner pull*\n'
        f'>Last pull: {label}\n'
        f'>Run NOW: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py carla`\n'
        f'>Contractor referral pipeline needs fresh contacts before June Booking Blitz.'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Carla staleness alert posted — {days_stale} days since last pull')


def _acquire_lock() -> bool:
    """Return True if we got the lock, False if another instance is running."""
    LOCK_FILE.parent.mkdir(exist_ok=True)
    if LOCK_FILE.exists():
        try:
            age = time.time() - LOCK_FILE.stat().st_mtime
            if age < LOCK_TIMEOUT_SECONDS:
                return False  # Another instance is running
        except Exception:
            pass
        LOCK_FILE.unlink(missing_ok=True)  # stale lock — remove
    try:
        LOCK_FILE.write_text(str(os.getpid()))
        return True
    except Exception:
        return False


def _release_lock():
    try:
        LOCK_FILE.unlink(missing_ok=True)
    except Exception:
        pass


def main():
    if not _acquire_lock():
        print('Another vera_relay instance is running — exiting.')
        return

    try:
        _main_body()
    finally:
        _release_lock()


def _flush_unpushed_commits():
    """Push any local commits not yet on remote before pulling.
    Without this, a failed push of the 'cleared pending_messages' commit means
    the next rebase applies that empty-file commit on top of new Vera messages,
    silently discarding them from Slack delivery."""
    result = git(['log', 'origin/main..HEAD', '--oneline'])
    unpushed = [l for l in result.stdout.strip().splitlines() if l.strip()]
    if not unpushed:
        return
    print(f'  Flushing {len(unpushed)} unpushed local commit(s) before pull...')
    push_result = git(['push', 'origin', 'main'])
    if push_result.returncode == 0:
        log(f'Flushed {len(unpushed)} unpushed commit(s) before pull')
    else:
        print(f'  ⚠️ Flush push failed: {push_result.stderr[:100]} — continuing with pull')


def _main_body():
    # Always check staleness (runs even if no new Vera commits)
    _check_danny_staleness()
    _check_carla_staleness()

    # Fetch first so origin/main is current before flush checks origin/main..HEAD
    git(['fetch', 'origin'])

    # Flush unpushed commits before pulling — prevents cleared-file rebase clobbering new messages
    _flush_unpushed_commits()

    # Pull latest
    git(['pull', '--rebase', 'origin', 'main'])

    # Get last known commit
    last_commit = STATE_FILE.read_text().strip() if STATE_FILE.exists() else ''

    # Get latest commit SHA
    result = git(['log', 'origin/main', '-20', '--format=%H|%an|%s'])
    commits = [line.split('|', 2) for line in result.stdout.strip().splitlines() if '|' in line]

    # Find new Vera commits since last run
    new_vera_commits = []
    for sha, author, subject in commits:
        if sha == last_commit:
            break
        if 'Vera Cole' in author or 'vera' in author.lower():
            new_vera_commits.append((sha, subject))

    if not new_vera_commits:
        print(f'No new Vera commits since {last_commit[:7] if last_commit else "start"}')
        return

    print(f'Found {len(new_vera_commits)} new Vera commit(s)')

    # Read pending messages
    if PENDING_FILE.exists():
        content = PENDING_FILE.read_text().strip()
        if content and len(content) > 10:
            messages = [m.strip() for m in content.split('---') if m.strip() and len(m.strip()) > 10]
            posted = 0
            for msg in messages[:50]:
                if post_slack(msg[:3000]):
                    posted += 1
            print(f'Posted {posted}/{len(messages)} messages to Slack')
            log(f'Relayed {posted} Vera messages to Slack')

            # Clear the file after posting
            try:
                PENDING_FILE.write_text('')
            except Exception as e:
                print(f'Warning: could not clear pending file: {e}')
            git(['add', str(PENDING_FILE.relative_to(BASE_DIR))])
            git(['commit', '-m', 'Vera Relay: cleared pending Slack messages after posting'])
            git(['push', 'origin', 'main'])
        else:
            # No pending messages — just post a summary of what Vera did
            latest_sha, latest_subject = new_vera_commits[0]
            post_slack(f'🔧 *Vera — Commit*\n>{latest_subject}')
            log(f'Posted Vera commit summary: {latest_subject}')
    else:
        # No pending file — post commit summary
        latest_sha, latest_subject = new_vera_commits[0]
        post_slack(f'🔧 *Vera — Commit*\n>{latest_subject}')
        log(f'Posted Vera commit summary: {latest_subject}')

    # Save last seen commit
    STATE_FILE.parent.mkdir(exist_ok=True)
    STATE_FILE.write_text(commits[0][0] if commits else '')


if __name__ == '__main__':
    main()
