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

BASE_DIR = Path(__file__).parent.parent.resolve()
PENDING_FILE = BASE_DIR / 'outputs' / 'vera' / 'pending_slack_messages.md'
STATE_FILE = BASE_DIR / 'outputs' / 'vera' / 'relay_last_commit.txt'
LOG_FILE = BASE_DIR / 'logs' / 'activity.log'

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
    """Read activity.log for last Danny pull. Post Slack alert if > 7 days. Once per day."""
    sentinel = BASE_DIR / 'outputs' / 'vera' / '.danny_alert_sent_date'
    today_str = datetime.now().strftime('%Y-%m-%d')

    if sentinel.exists() and sentinel.read_text().strip() == today_str:
        return  # Already alerted today

    last_pull_dt = None
    if LOG_FILE.exists():
        try:
            for line in reversed(LOG_FILE.read_text().splitlines()):
                if 'Danny' in line and 'Apollo pull' in line:
                    # Line format: [2026-05-12 08:00] Danny | ...
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
        sentinel.parent.mkdir(exist_ok=True)
        try:
            sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Danny staleness alert posted — {days_stale} days since last pull')


def main():
    # Always check Danny cron staleness (runs even if no new Vera commits)
    _check_danny_staleness()

    # Pull latest
    git(['fetch', 'origin'])
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
