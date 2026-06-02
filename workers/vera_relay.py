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
        f'>Run (auto-selects correct county this week): `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py danny`\n'
        f'>Round 2 enrollment: June 4.'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Danny staleness alert posted — {days_stale} days since last pull')


def _check_instantly_paused():
    """Warn Bradley once per day if Instantly.ai is not confirmed paused.
    Instantly.ai overlap = duplicate emails = spam filters = 0% reply rate on Round 2.
    Fires every morning until INSTANTLY_PAUSED=true is added to .env.
    """
    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.instantly_alert_sent_date'
    today_str = datetime.now().strftime('%Y-%m-%d')

    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return  # Already alerted today

    if os.environ.get('INSTANTLY_PAUSED', '').lower() == 'true':
        return  # Confirmed paused — no alert needed

    msg = (
        '⚠️ *Instantly.ai NOT Paused — Daily Reminder*\n'
        '>Campaigns a1c08c3d (PM Cuyahoga) + 626cd15d (Contractor Referral) are NOT confirmed paused.\n'
        '>Duplicate sends to Round 2 contacts = spam filters = 0% reply rate on June 4 enrollment.\n'
        '>\n'
        '>FIX (3 min): app.instantly.ai → Campaigns → ⋮ → Pause both campaigns\n'
        '>Then add  INSTANTLY_PAUSED=true  to your .env file\n'
        '>Guide: outputs/vera/instantly_pause_guide_2026-05-22.md'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log('Instantly.ai not-paused daily reminder posted to Slack')


def _check_nina_staleness():
    """Alert if Nina's daily hot leads report hasn't run in 2+ days — pipeline visibility gap."""
    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.nina_alert_sent_date'
    today_str = datetime.now().strftime('%Y-%m-%d')

    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    last_nina_dt = None
    if LOG_FILE.exists():
        try:
            for line in reversed(LOG_FILE.read_text().splitlines()):
                if 'Nina' in line and ('hot leads report' in line or 'workiz' in line.lower()):
                    date_part = line[1:11]
                    last_nina_dt = datetime.strptime(date_part, '%Y-%m-%d')
                    break
        except Exception:
            pass

    days_stale = (datetime.now() - last_nina_dt).days if last_nina_dt else 99
    if days_stale < 2:
        return

    label = last_nina_dt.strftime('%B %d') if last_nina_dt else 'unknown'
    msg = (
        f'📊 *Nina Cron Alert — {days_stale} days since last daily report*\n'
        f'>Last report: {label}\n'
        f'>Pipeline visibility gap — hot leads and due-today contacts not being surfaced.\n'
        f'>Run locally: `cd /Users/bradleyneal/forestcity && python3 workers/nina_report.py daily`\n'
        f'>Check cron: `cat logs/cron.log | tail -20`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Nina staleness alert posted — {days_stale} days since last report')


def _check_workiz_staleness():
    """Alert if no Workiz job report has run in 3+ days — revenue visibility gap."""
    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.workiz_alert_sent_date'
    today_str = datetime.now().strftime('%Y-%m-%d')

    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    last_workiz_dt = None
    if LOG_FILE.exists():
        try:
            for line in reversed(LOG_FILE.read_text().splitlines()):
                if 'Nina' in line and 'workiz' in line.lower():
                    date_part = line[1:11]
                    last_workiz_dt = datetime.strptime(date_part, '%Y-%m-%d')
                    break
        except Exception:
            pass

    days_stale = (datetime.now() - last_workiz_dt).days if last_workiz_dt else 99
    if days_stale < 3:
        return

    label = last_workiz_dt.strftime('%B %d') if last_workiz_dt else 'unknown'
    msg = (
        f'💼 *Workiz Cron Alert — {days_stale} days since last job report*\n'
        f'>Last report: {label}\n'
        f'>Revenue visibility gap — booked jobs and outstanding balances not being tracked.\n'
        f'>Run locally: `cd /Users/bradleyneal/forestcity && python3 workers/workiz_report.py daily`\n'
        f'>Check cron: `cat logs/cron.log | tail -20`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Workiz staleness alert posted — {days_stale} days since last report')


def _check_summit_deadline():
    """Fire a countdown alert daily May 27–May 31. Summit pull deadline is May 31.
    After May 31, Summit next auto-rotates June 29 (Week 27 % 6 = 3 = Summit index).
    """
    from datetime import date as _date_s
    today = _date_s.today()
    deadline = _date_s(2026, 5, 31)
    if today > deadline:
        return
    days_left = (deadline - today).days

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.summit_alert_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    urgency_emoji = '🚨' if days_left <= 1 else '⏰'
    days_label = 'TODAY — FINAL DAY' if days_left == 0 else f'{days_left} DAY{"S" if days_left != 1 else ""} LEFT'
    friday_note = (
        '\n>⚠️ FRIDAY = LAST BUSINESS DAY — run before EOD today or Saturday. Do NOT wait until Sunday.\n'
        '>6 min unattended: `python3 workers/lead_pipeline.py both Summit` — start it right now.'
    ) if today.weekday() == 4 else ''
    saturday_note = (
        '\n>⚠️ SATURDAY — Run it NOW before Sunday scramble. 6 min, fully unattended.\n'
        '>Do NOT wait until Sunday (May 31 = deadline day). Start before you do anything else today.'
    ) if today.weekday() == 5 else ''
    msg = (
        f'{urgency_emoji} *Summit County Pull — {days_label} (Deadline May 31)*\n'
        f'>Miss this window = no Summit leads until June 29 (next auto-rotation, Week 27).\n'
        f'>All 150+ commercial segments (restaurants, banks, gyms, hospitals, sports venues + more) miss peak season.\n'
        f'>Danny only: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py danny Summit`\n'
        f'>Danny + Carla (recommended): `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Summit`\n'
        f'>Or double-click: `scripts/run_summit_both.command` in Finder — both workers, one click.'
        f'{friday_note}{saturday_note}'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Summit County deadline countdown posted — {days_left} days left')


def _check_gas_station_pending():
    """Alert daily if gas_station contacts are in pipeline but sequence is still PENDING."""
    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.gas_station_pending_alert_date'
    today_str = datetime.now().strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    try:
        sys_path_saved = __import__('sys').path[:]
        __import__('sys').path.insert(0, str(BASE_DIR))
        from integrations.mixmax import SEQUENCES
        if SEQUENCES.get('gas_station', {}).get('id') != 'PENDING':
            return  # Sequence is live — no alert needed
    except Exception:
        return
    finally:
        try:
            __import__('sys').path[:] = sys_path_saved
        except Exception:
            pass

    pipeline_f = BASE_DIR / 'pipeline_data.json'
    cache_f = BASE_DIR / 'contacts_cache.json'
    import json as _json_gs
    gas_contacts = []
    for src_file, key in [(pipeline_f, 'manual_contacts'), (cache_f, 'contacts')]:
        if not src_file.exists():
            continue
        try:
            data = _json_gs.loads(src_file.read_text())
            gas_contacts += [
                c for c in data.get(key, [])
                if c.get('lead_type') == 'gas_station' or c.get('_lead_type') == 'gas_station'
            ]
        except Exception:
            pass

    if not gas_contacts:
        return

    msg = (
        f'⛽ *Gas Station Sequence Still PENDING — {len(gas_contacts)} contacts waiting*\n'
        f'>These {len(gas_contacts)} contacts cannot be enrolled until you create the Mixmax sequence (30 min).\n'
        f'>Setup guide: `outputs/danny/gas_station_sequence_create_now_2026-05-27.md`\n'
        f'>Or: Mixmax → Sequences → New → paste ID into `integrations/mixmax.py` line 54.\n'
        f'>⚡ **BYPASS TODAY:** Gmail blast guide ready — email all {len(gas_contacts)} contacts directly right now.\n'
        f'>File: `outputs/danny/gas_station_manual_email_blast_2026-05-19.md` — 3 templates + send schedule.'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Gas station PENDING alert posted — {len(gas_contacts)} contacts waiting')


def _check_fleet_sequence_pending():
    """Alert daily if fleet_washing sequence is still PENDING.
    Parallel to _check_gas_station_pending() — both sequences are PENDING and both
    may have stranded contacts in contacts_cache.json. Fleet contacts waiting for
    sequence ID since the sequence was added to integrations/mixmax.py."""
    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.fleet_pending_alert_date'
    today_str = datetime.now().strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    try:
        sys_path_saved = __import__('sys').path[:]
        __import__('sys').path.insert(0, str(BASE_DIR))
        from integrations.mixmax import SEQUENCES
        if SEQUENCES.get('fleet_washing', {}).get('id') != 'PENDING':
            return  # Sequence is live — no alert needed
    except Exception:
        return
    finally:
        try:
            __import__('sys').path[:] = sys_path_saved
        except Exception:
            pass

    # Check for stranded fleet contacts in cache or pipeline
    cache_file = BASE_DIR / 'contacts_cache.json'
    pipeline_file = BASE_DIR / 'pipeline_data.json'
    fleet_count = 0
    for src_file, key in [(cache_file, 'contacts'), (pipeline_file, 'manual_contacts')]:
        if not src_file.exists():
            continue
        try:
            import json as _json
            data = _json.loads(src_file.read_text())
            fleet_count += sum(
                1 for c in data.get(key, [])
                if c.get('_lead_type') == 'fleet_washing' or c.get('lead_type') == 'fleet_washing'
            )
        except Exception:
            pass

    msg = (
        f'🚛 *Fleet Washing Sequence Still PENDING — Create in Mixmax UI*\n'
        f'>Fleet sequence has been PENDING since the system launched. {fleet_count} fleet contacts waiting (if any).\n'
        f'>Create in Mixmax → Sequences → New → Name: "Forest City Power Washing — Fleet Washing Outreach"\n'
        f'>Paste the new ID into `integrations/mixmax.py` line ~48 (fleet_washing id field).\n'
        f'>Then run: `python3 workers/lead_pipeline.py pending` to auto-enroll waiting contacts.\n'
        f'>Sequence copy: `outputs/danny/sequence_fleet_washing_2026-05-18.md`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log('Fleet washing PENDING sequence alert posted')


def _check_carla_staleness():
    """Check when Carla last ran. Post Slack alert if > 8 days (same cadence as Danny). Once per day."""
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
    if days_stale < 8:
        return

    label = last_pull_dt.strftime('%B %d') if last_pull_dt else 'unknown'
    msg = (
        f'🟣 *Carla Cron Alert — {days_stale} days since last referral partner pull*\n'
        f'>Last pull: {label}\n'
        f'>Run (auto-selects correct county this week): `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py carla`\n'
        f'>Contractor referral pipeline needs fresh contacts before June Booking Blitz (June 4).'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Carla staleness alert posted — {days_stale} days since last pull')


def _check_ad_lead_log_reminder():
    """During Week 1 after ad launch (May 26 – June 1), remind Bradley once/day to fill in the lead log.
    Every lead that isn't logged = invisible CPA math = can't know if ads are working at the job level.
    Auto-deactivates after June 1.
    """
    from datetime import date as _date_ad
    today = _date_ad.today()
    launch_date = _date_ad(2026, 5, 26)
    end_date = _date_ad(2026, 6, 1)
    if today < launch_date or today > end_date:
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.ad_log_reminder_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    day_num = (today - launch_date).days + 1
    msg = (
        f'📊 *Ad Launch — Day {day_num} Lead Log Reminder*\n'
        f'>Every Facebook + Google lead needs to be logged today: name, source, response time, quoted Y/N, booked Y/N.\n'
        f'>Log: `outputs/rick/launch_week_lead_log_2026-05-26.md` (or use Nina\'s ad_lead_tracker guide)\n'
        f'>Without this, Google Ads optimizes toward clicks not bookings — and you can\'t see CPA.\n'
        f'>Day 3 check (May 28): `outputs/vera/day3_ads_check_card_2026-05-26.md`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Ad lead log reminder posted — Day {day_num} of launch week')


def _check_medina_reminder():
    """Fire Medina County pull reminder May 29–June 4 (pull due June 1, needed for June 4 enrollment).
    Start date corrected from May 30 → May 29 (Run 138): May 29 is the last Friday before the pull
    weekend — Bradley needs the Friday heads-up, not just Saturday morning."""
    from datetime import date as _date_m
    today = _date_m.today()
    start = _date_m(2026, 5, 29)
    end   = _date_m(2026, 6, 4)
    if not (start <= today <= end):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.medina_alert_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    days_to_june1 = (_date_m(2026, 6, 1) - today).days
    if days_to_june1 > 0:
        label = f'{days_to_june1} day{"s" if days_to_june1 != 1 else ""} away'
        note  = f'Medina pull opens in {label} — stage your shortcut now.'
    elif days_to_june1 == 0:
        label = 'TODAY'
        note  = 'Run it now — June 4 enrollment needs fresh Medina leads.'
    else:
        days_late = abs(days_to_june1)
        label = f'{days_late} day{"s" if days_late != 1 else ""} overdue'
        note  = f'Medina pull is {label} — run immediately to have leads ready for June 4 enrollment.'

    msg = (
        f'📍 *Medina County Pull — {label}*\n'
        f'>{note}\n'
        f'>Command: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Medina`\n'
        f'>Or double-click: `scripts/run_medina_both.command` in Finder\n'
        f'>Guide: `outputs/donna/june1_medina_pull_guide_2026-05-26.md`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Medina County pull reminder posted — {label}')


def _check_day7_ads_review():
    """Fire Day 7 ads scaling review on June 2 (7 days after May 26 launch)."""
    from datetime import date as _date_ad7
    today = _date_ad7.today()
    if today != _date_ad7(2026, 6, 2):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.day7_ads_alert_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    msg = (
        '📊 *Ads Day 7 — Week 2 Scaling Decision (June 2)*\n'
        '>7 days since launch (May 26). Time for the full Week 2 scaling review.\n'
        '>Facebook review: `outputs/rick/facebook_ads_first_week_monitoring_guide_2026-05-23.md`\n'
        '>Google review: `outputs/rick/google_ads_first_week_monitoring_guide_2026-05-24.md`\n'
        '>Week 2 scaling decision matrix: `outputs/rick/week2_facebook_ads_scaling_guide_2026-05-26.md`\n'
        '>If CTR >1.5% + CPL <$30 → bump budget 20%. Mixed → creative swap. Not working → diagnostic.'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log('Day 7 ads scaling review reminder posted')


def _check_june4_enrollment_countdown():
    """Fire June 4 Round 2 enrollment countdown on June 2 and June 3 (pre-flight reminders)."""
    from datetime import date as _date_j4
    today = _date_j4.today()
    start = _date_j4(2026, 6, 1)
    end   = _date_j4(2026, 6, 3)
    if not (start <= today <= end):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.june4_enrollment_alert_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    days_left = (_date_j4(2026, 6, 4) - today).days
    label = 'TOMORROW' if days_left == 1 else f'{days_left} days away'

    msg = (
        f'🚀 *June 4 Round 2 Enrollment — {label}*\n'
        f'>Round 2 = Medina+Summit PM enrollment + gas station enrollment + contractor text blast.\n'
        f'>Night-before checklist: `outputs/donna/june3_tuesday_evening_checklist_2026-05-26.md`\n'
        f'>Battle card (June 4 morning): `outputs/donna/june4_enrollment_battle_card_2026-05-24.md`\n'
        f'>GO/NO-GO tracker: `outputs/vera/june4_enrollment_readiness_tracker_2026-05-27.md`\n'
        f'>Verify: Instantly.ai paused ✓ | Medina pull done ✓ | Summit pull done ✓ | Gas station sequence created ✓'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'June 4 enrollment countdown posted — {label}')


def _check_day3_ads_check():
    """Fire specifically on May 28 — Day 3 after May 26 launch.
    Day 3 is the FIRST allowed tweak window for Facebook algorithm (touching before Day 3 resets learning phase).
    One-time, self-deactivating."""
    from datetime import date as _date_d3
    today = _date_d3.today()
    if today != _date_d3(2026, 5, 28):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.day3_ads_alert_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    msg = (
        '📊 *Ads Day 3 — First Tweak Window (May 28)*\n'
        '>Day 3 is the FIRST day you\'re allowed to touch the Facebook campaign without resetting the algorithm learning phase.\n'
        '>Facebook thresholds: CTR <1% = check creative | CPL >$50 = check audience | Reach <500 = check budget\n'
        '>Google thresholds: CTR <2% = check keywords/ads | CPC >$8 = pause low-quality keywords\n'
        '>One-tweak rule: if adjusting, change ONE thing only (creative OR audience OR budget — never all three)\n'
        '>If numbers are acceptable → leave it alone. Facebook needs 7 days to optimize.\n'
        '>Full check card: `outputs/vera/day3_ads_check_card_2026-05-26.md`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log('Ads Day 3 first-tweak-window reminder posted')


def _check_wave2_contractor_blitz():
    """Fire ONLY on May 28 — the 16 Wave 2 contractor first-touch text day.
    Provides the blitz card reference and contact count. One-time, self-deactivating."""
    from datetime import date as _date_w2
    today = _date_w2.today()
    if today != _date_w2(2026, 5, 28):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.wave2_blitz_alert_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    msg = (
        '📲 *Wave 2 Contractor Blitz — TODAY (May 28)*\n'
        '>16 first-touch texts are due today to Wave 2 landscapers + construction contractors.\n'
        '>Blitz card (3 copy-paste texts by trade type): `outputs/vera/wave2_contractor_blitz_may28_2026-05-27.md`\n'
        '>Follow-up schedule (Day 3 May 31, Day 7 June 4): `outputs/vera/wave2_contractor_followup_schedule_2026-05-27.md`\n'
        '>Tip: run Summit pull first (6 min unattended), send texts WHILE it runs = zero wasted time.'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log('Wave 2 contractor blitz reminder posted (May 28 only)')


def _check_past_customer_blast():
    """Fire daily May 27–June 7: remind Bradley that past customers are the fastest revenue path
    while Google/Facebook ads are in the 7-day learning phase and generating 0-2 leads/day.
    Tommy wrote the guide May 27. Zero excuses not to send 10 texts in 30 minutes.
    Self-deactivates June 8."""
    from datetime import date as _date_pc
    today = _date_pc.today()
    start = _date_pc(2026, 5, 27)
    end   = _date_pc(2026, 6, 7)
    if not (start <= today <= end):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.past_customer_blast_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    msg = (
        '💰 *Past Customer Blast — Fastest Revenue This Week*\n'
        '>Ads are in learning phase (7 days, $0–2 leads/day right now). Fastest revenue = past customers.\n'
        '>30 minutes of texts → $1,800–$3,000 in booked jobs based on typical re-engagement rates.\n'
        '>Guide + 5 copy-paste text scripts by scenario: `outputs/tommy/past_customer_june_blast_2026-05-27.md`\n'
        '>Look up past customers in Workiz → text the ones from 2025 + spring 2026 who haven\'t rebooked.'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log('Past customer blast reminder posted')


def _check_ad_lead_day5_escalation():
    """Fire on May 31 (Day 5 after May 26 launch) with an escalated alert if NO ad leads
    are logged in pipeline_data.json. By Day 5 there should be at least 1-3 logged leads
    if ads are working. Zero logged = either no leads or they're going un-logged.
    One-time, self-deactivating."""
    from datetime import date as _date_d5
    today = _date_d5.today()
    if today != _date_d5(2026, 5, 31):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.ad_day5_escalation_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    # Check if any ad leads are logged in pipeline_data.json
    pipeline_f = BASE_DIR / 'pipeline_data.json'
    ad_lead_count = 0
    if pipeline_f.exists():
        try:
            import json as _json
            pd = _json.loads(pipeline_f.read_text())
            for c in pd.get('manual_contacts', []):
                src = (c.get('lead_source', '') or '').lower()
                if 'facebook' in src or 'google' in src or 'ad' in src or 'fb' in src:
                    ad_lead_count += 1
        except Exception:
            pass

    if ad_lead_count > 0:
        return  # Leads are being logged — no escalation needed

    msg = (
        '🚨 *Ads Day 5 — Zero Leads Logged in Pipeline (May 31)*\n'
        '>5 days since launch (May 26). No Facebook or Google ad leads found in pipeline_data.json.\n'
        '>Two possibilities:\n'
        '>  1. Ads haven\'t generated leads yet (check Facebook Lead Center + Google Ads → Conversions)\n'
        '>  2. Leads came in but weren\'t logged (check Workiz for booked jobs this week)\n'
        '>Action (5 min): Check Facebook Business Suite → Leads Center for form fills this week.\n'
        '>If leads exist but aren\'t logged: `outputs/nina/ad_lead_tracker_2026-05-26.md` (30-sec log process)\n'
        '>If zero leads in FB Lead Center: Day 5 diagnostic in `outputs/vera/day3_ads_check_card_2026-05-26.md`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log('Ad lead Day 5 escalation alert posted — 0 ad leads logged after 5 days')


def _check_june4_enrollment_day():
    """Fire ONLY on June 4 — enrollment day itself. Provides the step-by-step morning game plan:
    run Medina + Summit batches, check Instantly paused, fire enrollment script.
    Separate from the pre-flight countdown (June 2-3) — this fires on the day, not before it.
    One-time, self-deactivating."""
    from datetime import date as _date_j4d
    today = _date_j4d.today()
    if today != _date_j4d(2026, 6, 4):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.june4_enrollment_day_sent'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    msg = (
        '🚀 *IT\'S JUNE 4 — ROUND 2 ENROLLMENT DAY*\n'
        '>Step 1: Verify Instantly.ai campaigns a1c08c3d + 626cd15d are PAUSED (app.instantly.ai → Campaigns → ⋮ → Pause)\n'
        '>Step 2: Run Medina batch: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Medina`\n'
        '>Step 3: Run Summit batch: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Summit`\n'
        '>Step 4: Check contacts_cache.json total — confirm new leads are appended\n'
        '>Step 5: Review Nina\'s report: `python3 workers/nina_report.py daily` — any hot leads from Round 1 to call first?\n'
        '>Step 6: Gas station contacts — if sequence ID is pasted into mixmax.py, they enroll automatically. If not, Gmail blast today.\n'
        '>Full battle card: `outputs/donna/june4_enrollment_battle_card_2026-05-24.md`\n'
        '>GO/NO-GO tracker: `outputs/vera/june4_enrollment_readiness_tracker_2026-05-27.md`\n'
        '>This is the biggest outreach day of peak season. Execute in order. Don\'t skip Step 1.'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log('June 4 enrollment day game plan posted')


def _check_post_june4_monitoring():
    """Fire daily June 5–11: remind Bradley that Round 2 emails are actively sending,
    check Nina hot leads report daily, respond to replies within 24 hours.
    Round 2 Day 3 (June 7) = first opens/replies expected. Self-deactivates June 12."""
    from datetime import date as _date_j4m
    today = _date_j4m.today()
    start = _date_j4m(2026, 6, 5)
    end   = _date_j4m(2026, 6, 11)
    if not (start <= today <= end):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.post_june4_monitor_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    day_num = (today - start).days + 2  # June 5 = Day 2 post-enrollment
    msg = (
        f'📬 *Round 2 Sequence — Day {day_num} (Post-Enrollment)*\n'
        f'>Enrolled contacts are actively receiving emails. First opens/replies expected June 7–9.\n'
        f'>Run Nina\'s daily report locally: `cd /Users/bradleyneal/forestcity && python3 workers/nina_report.py daily`\n'
        f'>When someone REPLIES → respond within 24 hours → book the call or estimate\n'
        f'>Hot leads (2+ opens, no reply) → connect on LinkedIn same day → message: "saw you opened our email"\n'
        f'>Sequence cadence: Touch 1 (Day 0) → Touch 2 (Day 3) → Touch 3 (Day 7) → let Nina surface the hot ones'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Post-June 4 sequence monitoring reminder posted — Day {day_num}')


def _check_wave2_day3_followup():
    """Fire ONLY on May 31 — Day 3 after Wave 2 contractor first-touch texts (May 28).
    Day 3 is the follow-up window: not so soon it's annoying, not so late they've forgotten.
    One-time, self-deactivating. May 31 is also the Summit pull deadline — two birds, one day."""
    from datetime import date as _date_w2d3
    today = _date_w2d3.today()
    if today != _date_w2d3(2026, 5, 31):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.wave2_day3_followup_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    msg = (
        '📲 *Wave 2 Contractor Follow-Up — Day 3 (May 31)*\n'
        '>16 Wave 2 contractors received first-touch texts Thursday May 28. Today = Day 3 follow-up window.\n'
        '>Follow up with anyone who opened but didn\'t reply — or no response at all:\n'
        '>  "Hey [name], wanted to follow up from Thursday. Worth a quick chat about referring each other?\n'
        '>   I refer your services to our customers, you refer ours. No paperwork, just a $50 referral deal."\n'
        '>Full Day 3 scripts by trade: `outputs/vera/wave2_contractor_followup_schedule_2026-05-27.md`\n'
        '>ALSO TODAY: Summit County pull deadline (last chance). Run while texts are sending — 6 min unattended.'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log('Wave 2 contractor Day 3 follow-up reminder posted (May 31 only)')


def _check_june8_geauga_portage():
    """Fire June 4–8 countdown for the Cuyahoga County pull (Week 24, June 8 Monday).
    Week 24 % 6 = 0 → Cuyahoga in the rotation. Cleveland, Parma, Lakewood, Strongsville, Beachwood.
    LARGEST market — hospitals, museums, YMCA of Greater Cleveland, DSOs, government buildings.
    Function name retained for sentinel file compatibility (created before Run 118 date correction)."""
    from datetime import date as _date_gp
    today = _date_gp.today()
    start = _date_gp(2026, 6, 4)
    end   = _date_gp(2026, 6, 8)
    if not (start <= today <= end):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.geauga_portage_alert_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    pull_date = _date_gp(2026, 6, 8)
    days_left = (pull_date - today).days
    if days_left > 0:
        label = f'{days_left} day{"s" if days_left != 1 else ""} away'
        note = 'Cron fires Mon June 8 at 7am. Verify: `cat logs/cron.log | tail -10`'
    else:
        label = 'TODAY — CUYAHOGA (BIGGEST MARKET)'
        note = 'Run now if cron missed: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Cuyahoga`'

    msg = (
        f'🏙️ *Cuyahoga County Pull — {label} (June 8) — LARGEST MARKET*\n'
        f'>Week 24 rotation: Cleveland, Parma, Lakewood, Strongsville, Beachwood. Highest lead volume of all 6 counties.\n'
        f'>All 150+ commercial segments fire here: hospitals (Cleveland Clinic, UH, MetroHealth), museums\n'
        f'>   (Cleveland Museum of Art, Metroparks Zoo, Rock Hall), YMCA of Greater Cleveland (12 branches),\n'
        f'>   DSO chains (Aspen Dental, Heartland), government/transit (GCRTA, Port of Cleveland, city halls),\n'
        f'>   dialysis (DaVita/Fresenius 50+ centers), concert venues (Blossom, Jacobs Pavilion),\n'
        f'>   dollar stores (DG/FD/DT 300+ locations), auto parts (O\'Reilly/AutoZone/NAPA), hardware\n'
        f'>   (Home Depot/Lowe\'s), sports venues (Cavs/Guardians/Browns), cannabis dispensaries,\n'
        f'>   blood/plasma centers, coin laundries, warehouse clubs (Costco/Sam\'s), wireless retail,\n'
        f'>   wineries/distilleries, motorcycle/powersport dealers, RV/camper dealers, garden centers,\n'
        f'>   marine/boat dealers, ice cream chains (Dairy Queen/Handel\'s), party/event rental,\n'
        f'>   trampoline parks (Sky Zone/Urban Air/Scene75), moving companies (Two Men and a Truck),\n'
        f'>   off-price retail (TJ Maxx/Marshalls/HomeGoods/Burlington), truck rental (U-Haul/Penske/Ryder),\n'
        f'>   used car lots (CarMax/DriveTime/independent), outdoor power equipment (STIHL/Husqvarna/Cub Cadet),\n'
        f'>   vocational & trade schools (CVCC/Ohio Technical College/Auburn CTE),\n'
        f'>   summer day camps & youth programs (Boys & Girls Club, Camp Cheerful) + more.\n'
        f'> ✅ Title + org keyword batching active (Run 134+): all 150+ segments fully queried.\n'
        f'>{note}\n'
        f'>Shortcut: double-click `scripts/run_cuyahoga_both.command` in Finder (no typing required)\n'
        f'>Command: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Cuyahoga`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Cuyahoga June 8 pull reminder posted — {label}')


def _check_june22_lake_county():
    """Fire June 18–22 countdown for the Lorain County pull (Week 26, June 22 Monday).
    Week 26 % 6 = 2 → Lorain in the rotation. Elyria, Avon, North Ridgeville, Vermilion.
    Avon = fastest-growing NE Ohio suburb; strong HOA density + Rt 83 industrial corridor.
    Function name retained for sentinel file compatibility (created before Run 118 date correction)."""
    from datetime import date as _date_lk
    today = _date_lk.today()
    start = _date_lk(2026, 6, 18)
    end   = _date_lk(2026, 6, 22)
    if not (start <= today <= end):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.lake_county_alert_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    pull_date = _date_lk(2026, 6, 22)
    days_left = (pull_date - today).days
    if days_left > 0:
        label = f'{days_left} day{"s" if days_left != 1 else ""} away'
        note = f'Cron fires Mon June 22 at 7am. Verify: `cat logs/cron.log | tail -10`'
    else:
        label = 'TODAY — LORAIN COUNTY (AVON CORRIDOR)'
        note = 'Run now if cron missed: `python3 workers/lead_pipeline.py both Lorain`'

    msg = (
        f'📍 *Lorain County Pull — {label} (June 22)*\n'
        f'>Week 26 rotation: Elyria, Avon, North Ridgeville, Vermilion. Avon = fastest-growing NE Ohio suburb.\n'
        f'>High HOA density in new Avon subdivisions. Lorain Harbor marina corridor + Vermilion Lake Erie shoreline.\n'
        f'>Also: industrial corridor along Rt 83 (self-storage, auto body, distribution), Invacare (Elyria) campus.\n'
        f'>{note}\n'
        f'>Command: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Lorain`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Lorain County June 22 pull reminder posted — {label}')


def _check_june15_cuyahoga():
    """Fire June 11–15 countdown for the Lake County pull (Week 25, June 15 Monday).
    Week 25 % 6 = 1 → Lake in the rotation. Mentor, Willoughby, Painesville, Lake Erie shoreline.
    MARINA segment — Mentor Harbor, Sheffield Lake, Euclid shoreline, Lorain County marinas.
    Function name retained for sentinel file compatibility (created before Run 118 date correction)."""
    from datetime import date as _date_cy
    today = _date_cy.today()
    start = _date_cy(2026, 6, 11)
    end   = _date_cy(2026, 6, 15)
    if not (start <= today <= end):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.cuyahoga_june15_alert_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    pull_date = _date_cy(2026, 6, 15)
    days_left = (pull_date - today).days
    if days_left > 0:
        label = f'{days_left} day{"s" if days_left != 1 else ""} away'
        note = 'Cron fires Mon June 15 at 7am. Verify: `cat logs/cron.log | tail -10`'
    else:
        label = 'TODAY — LAKE COUNTY (MARINA)'
        note = 'Run now if cron missed: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Lake`'

    msg = (
        f'⚓ *Lake County Pull — {label} (June 15) — MARINA CORRIDOR*\n'
        f'>Week 25 rotation: Mentor, Willoughby, Painesville + Lake Erie shoreline.\n'
        f'>Marina segment: Mentor Harbor, Sheffield Lake, Euclid shoreline — pre-season marina cleaning window.\n'
        f'>Marine/Boat Dealers: Skipper Buds (Mentor/Lorain), Inland Seas Yachts (Vermilion) — FIRST PULL this run.\n'
        f'>Also: hotel chains (Mentor/Willoughby corridor), senior living, fitness centers (Lake County YMCAs).\n'
        f'> ✅ Title + org keyword batching active (Run 134+): all 150+ segments fully queried.\n'
        f'>{note}\n'
        f'>Command: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Lake`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Lake County June 15 pull reminder posted — {label}')


def _check_june29_lorain():
    """Fire June 25–29 countdown for the Summit County pull (Week 27, June 29 Monday).
    Week 27 % 6 = 3 → Summit in the rotation. Akron, Fairlawn, Stow, Cuyahoga Falls, Hudson.
    Second pass through Summit — all commercial segments now include full title + org keyword batching.
    Function name retained for sentinel file compatibility (created before Run 118 date correction)."""
    from datetime import date as _date_lo
    today = _date_lo.today()
    start = _date_lo(2026, 6, 25)
    end   = _date_lo(2026, 6, 29)
    if not (start <= today <= end):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.lorain_june29_alert_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    pull_date = _date_lo(2026, 6, 29)
    days_left = (pull_date - today).days
    if days_left > 0:
        label = f'{days_left} day{"s" if days_left != 1 else ""} away'
        note = 'Cron fires Mon June 29 at 7am — verify it\'s running: `cat logs/cron.log | tail -10`'
    else:
        label = 'TODAY — SUMMIT COUNTY (AKRON CORRIDOR)'
        note = 'Run now if cron missed: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Summit`'

    msg = (
        f'📍 *Summit County Pull — {label} (June 29)*\n'
        f'>Week 27 rotation: Akron, Fairlawn, Stow, Cuyahoga Falls, Hudson.\n'
        f'>Firestone Country Club corridor, Akron Children\'s Hospital, Summa Health Akron City, Stan Hywet.\n'
        f'>Also: distribution hubs (Stow/Macedonia area), auto body (Caliber/CARSTAR), golf courses.\n'
        f'>{note}\n'
        f'>Command: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Summit`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Lorain June 29 pull reminder posted — {label}')


def _check_july6_medina():
    """Fire June 30–July 6 countdown for the Medina County pull (Week 28, July 6 Monday).
    Week 28 % 6 = 4 → Medina in the rotation. Medina, Brunswick, Wadsworth, Seville.
    July is peak power washing season — Medina's mid-size commercial + residential HOA market.
    Without this reminder, the July restart has no relay coverage and Bradley could miss it."""
    from datetime import date as _date_m6
    today = _date_m6.today()
    start = _date_m6(2026, 6, 30)
    end   = _date_m6(2026, 7, 6)
    if not (start <= today <= end):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.july6_medina_alert_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    pull_date = _date_m6(2026, 7, 6)
    days_left = (pull_date - today).days
    if days_left > 0:
        label = f'{days_left} day{"s" if days_left != 1 else ""} away'
        note = 'Cron fires Mon July 6 at 7am. Verify: `cat logs/cron.log | tail -10`'
    else:
        label = 'TODAY — MEDINA COUNTY (JULY RESTART)'
        note = 'Run now if cron missed: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Medina`'

    msg = (
        f'📍 *Medina County Pull — {label} (July 6) — JULY ROTATION RESTARTS*\n'
        f'>Week 28 rotation: Medina, Brunswick, Wadsworth. July = peak season — highest booking velocity.\n'
        f'>July Medina pull: fresh Medina leads for the second half of peak season. All segments now active.\n'
        f'>After this: Week 29 = Geauga+Portage (July 13), Week 30 = Cuyahoga (July 20).\n'
        f'>{note}\n'
        f'>Command: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Medina`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'July 6 Medina pull reminder posted — {label}')


def _check_post_june11_monitoring():
    """Fire daily June 12–30. Round 2 sequence replies trickle in for 21 days post-enrollment.
    The post_june4_monitoring() covers June 5–11. This bridges June 12–30 so Bradley never goes
    dark on a sequence that is still actively delivering and generating replies."""
    from datetime import date as _date_pm
    today = _date_pm.today()
    start = _date_pm(2026, 6, 12)
    end   = _date_pm(2026, 6, 30)
    if not (start <= today <= end):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.post_june11_monitor_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    day_num = (today - _date_pm(2026, 6, 4)).days + 1  # Day relative to June 4 enrollment
    msg = (
        f'📬 *Round 2 Sequence — Day {day_num} (Keep Monitoring)*\n'
        f'>Replies trickle in for up to 21 days post-enrollment — don\'t go dark after June 11.\n'
        f'>Run Nina\'s daily report: `cd /Users/bradleyneal/forestcity && python3 workers/nina_report.py daily`\n'
        f'>Respond to ANY reply within 24 hours — late replies are often the most qualified prospects.\n'
        f'>Hot leads (2+ opens, no reply): LinkedIn connect + "saw you opened our email" message.'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Post-June 11 sequence monitoring reminder posted — Day {day_num}')


def _check_review_request_reminder():
    """Fire daily during peak season May 28 – Sept 30.
    After every completed job, Bradley should send a Google review request text.
    Google reviews → higher Maps + LSA ranking → more inbound leads.
    Most NE Ohio power washing competitors sit at 25–50 reviews. Hitting 75+ breaks away.
    Self-deactivates Oct 1.
    """
    from datetime import date as _date_rr
    today = _date_rr.today()
    start = _date_rr(2026, 5, 28)
    end   = _date_rr(2026, 9, 30)
    if not (start <= today <= end):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.review_request_reminder_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    msg = (
        '⭐ *Google Review Request — Send After Today\'s Jobs*\n'
        '>Every completed job = a chance for a 5-star review. Most NE Ohio competitors: 25–50 reviews.\n'
        '>At 75+ Forest City enters top-tier ranking on Google Maps and LSA — that\'s free inbound leads.\n'
        '>Text template (30 sec per customer):\n'
        '>  "Hey [Name], Bradley here from Forest City Power Washing. Hope everything looks great!\n'
        '>   If you have 30 seconds, would mean the world if you left a quick Google review:\n'
        '>   [your Google Maps review link]  Thanks so much!"\n'
        '>Get your review link: Google Maps → search "Forest City Power Washing" → Reviews → "Get more reviews" → Copy link.\n'
        '>Target: 5 review requests/week = 100+ new reviews by end of season.'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log('Review request daily reminder posted to Slack')


def _check_pipeline_overdue_contacts():
    """Fire daily. Reads pipeline_data.json and surfaces all contacts with a past-due
    next_followup date. 36 contacts were sitting overdue with no Slack alert — this closes
    the operational gap between the pipeline existing and Bradley actually acting on it.
    Posts daily with a dedupe sentinel. Self-refreshes every calendar day."""
    from datetime import date as _date_po
    import json as _json_po
    today = _date_po.today()

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.pipeline_overdue_alert_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    pipeline_file = BASE_DIR / 'pipeline_data.json'
    if not pipeline_file.exists():
        return

    try:
        data = _json_po.loads(pipeline_file.read_text())
        contacts = data.get('manual_contacts', [])
    except Exception:
        return

    skip_stages = {'Closed Won', 'Closed Lost'}
    overdue = []
    no_date = []

    for c in contacts:
        stage = c.get('stage', '')
        if stage in skip_stages:
            continue
        nf = (c.get('next_followup') or '').strip()
        company = c.get('company') or f"{c.get('first_name','')} {c.get('last_name','')}".strip() or 'Unknown'
        lead_type = c.get('lead_type', '')
        if not nf:
            no_date.append((company, stage, lead_type))
        else:
            try:
                nf_date = _date_po.fromisoformat(nf[:10])
                if nf_date <= today:
                    overdue.append((company, stage, nf, lead_type))
            except Exception:
                no_date.append((company, stage, lead_type))

    total = len(overdue) + len(no_date)
    if total == 0:
        return

    lines = [f'📋 *Pipeline Follow-Up Due — {total} Contact{"s" if total != 1 else ""} Need Action Today*']

    if overdue:
        lines.append(f'>*Overdue ({len(overdue)}):*')
        for company, stage, nf, ltype in sorted(overdue, key=lambda x: x[2])[:8]:
            lines.append(f'>  • {company} ({stage}) — was due {nf}')
        if len(overdue) > 8:
            lines.append(f'>  … and {len(overdue) - 8} more overdue')

    if no_date:
        lines.append(f'>*No follow-up date set ({len(no_date)}):*')
        for company, stage, ltype in no_date[:5]:
            lines.append(f'>  • {company} ({stage})')
        if len(no_date) > 5:
            lines.append(f'>  … and {len(no_date) - 5} more without dates')

    gas_count = sum(1 for c in overdue if c[3] == 'gas_station') + sum(1 for c in no_date if c[2] == 'gas_station')
    if gas_count:
        lines.append(f'>⛽ {gas_count} gas station contacts need Mixmax sequence before enrolling — guide: `outputs/danny/gas_station_sequence_create_now_2026-05-27.md`')

    lines.append(f'>Update pipeline: `python3 scripts/contact_done.py` or edit pipeline_data.json directly.')

    msg = '\n'.join(lines)
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Pipeline overdue contacts alert posted — {total} contacts need action')


def _check_wave2_day7_followup():
    """Fire June 3–4 — Day 7 follow-up for Wave 2 contractor first-touch texts (sent May 28).
    Day 7 is the final warm touch before contacts move to cold cadence.
    Fires June 3 as a heads-up, June 4 as the action day (also Round 2 enrollment day)."""
    from datetime import date as _date_w2d7
    today = _date_w2d7.today()
    start = _date_w2d7(2026, 6, 3)
    end   = _date_w2d7(2026, 6, 4)
    if not (start <= today <= end):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.wave2_day7_followup_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    msg = (
        '📲 *Wave 2 Contractor — Day 7 Final Follow-Up (June 3–4)*\n'
        '>Wave 2 texts went out May 28. Day 7 = final warm touch before contacts go cold.\n'
        '>Script for no-reply contacts:\n'
        '>  "Hey [name], just checking in one more time. We refer our customers to local contractors they can trust —\n'
        '>   happy to send work your way if you\'re open to a quick intro. No pressure either way."\n'
        '>For Day 3 replies that went warm — push to a 10-min call today or tomorrow.\n'
        '>Full follow-up schedule: `outputs/vera/wave2_contractor_followup_schedule_2026-05-27.md`\n'
        '>ALSO TODAY: June 4 = Round 2 enrollment day. Battle card: `outputs/donna/june4_enrollment_battle_card_2026-05-24.md`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log('Wave 2 contractor Day 7 follow-up reminder posted (June 3–4 window)')


def _check_instagram_reminder():
    """Fire June 1–2 only. Jasmine built a 15-minute Instagram launch guide that has gone unused.
    Instagram is the highest-reach platform for before/after content — 3–5× organic reach vs Facebook.
    Forest City has zero Instagram presence heading into peak season.
    One-time reminder, self-deactivates June 3."""
    from datetime import date as _date_ig
    today = _date_ig.today()
    start = _date_ig(2026, 6, 1)
    end   = _date_ig(2026, 6, 2)
    if not (start <= today <= end):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.instagram_reminder_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    msg = (
        '📸 *Instagram Launch — 15 Minutes, Zero Cost, Free Reach All Season*\n'
        '>Jasmine\'s press-GO guide: `outputs/jasmine/instagram_launch_today_2026-05-26.md`\n'
        '>Steps: Create Business Account → paste bio → post first before/after photo. 15 min.\n'
        '>Before/after content gets 3–5× the organic reach on Instagram vs the same Facebook post.\n'
        '>No content calendar needed yet — just launch the account so it\'s live when job photos start rolling in.\n'
        '>Every day without an account = reach left on the table during peak season.'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log('Instagram launch reminder posted (June 1–2 one-time window)')


def _check_annual_plan_pitch_reminder():
    """Fire every Monday June–September. Open issue since Run 88 — Annual Plan is never pitched on calls.
    Annual Plan is Forest City's highest-LTV product (2× revenue per customer, recurring).
    One Monday reminder = 20+ opportunities per week to pitch it. One sentence is all it takes.
    Self-deactivates October 1."""
    from datetime import date as _date_ap
    today = _date_ap.today()
    start = _date_ap(2026, 6, 1)
    end   = _date_ap(2026, 9, 30)
    if not (start <= today <= end):
        return
    if today.weekday() != 0:  # Monday only
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.annual_plan_reminder_week'
    week_str = today.strftime('%Y-W%W')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == week_str:
        return

    msg = (
        '📋 *This Week: Pitch the Annual Plan on Every Quote Call*\n'
        '>Annual Plan = 2 visits (spring + fall), one price, recurring customer. Highest-LTV product.\n'
        '>One sentence close: "We also do an Annual Plan — spring wash + fall wash, one price,\n'
        '>  you just call us each season. Most of our regulars do it. Want me to add it as an option?"\n'
        '>Add "Annual Plan" as a line item in Workiz so it appears on every estimate automatically.\n'
        '>Full quote conversion kit: `outputs/tommy/quote_to_close_kit_2026-05-21.md`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(week_str)
        except Exception:
            pass
        log(f'Annual Plan pitch weekly reminder posted — week {week_str}')


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


def _check_july13_geauga_portage():
    """Fire July 7–13 countdown for Geauga+Portage pull (Week 29, July 13 Monday).
    Week 29 % 6 = 5 → Geauga+Portage in the rotation. Chardon, Painesville Township,
    Portage County (Kent, Ravenna, Streetsboro, Aurora). Second cycle of peak season.
    Without this reminder July relay coverage has a gap after Week 28 Medina."""
    from datetime import date as _date_gp
    today = _date_gp.today()
    start = _date_gp(2026, 7, 7)
    end   = _date_gp(2026, 7, 13)
    if not (start <= today <= end):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.july13_geauga_portage_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    pull_date = _date_gp(2026, 7, 13)
    days_left = (pull_date - today).days
    if days_left > 0:
        label = f'{days_left} day{"s" if days_left != 1 else ""} away'
        note = 'Cron fires Mon July 13 at 7am. Verify: `cat logs/cron.log | tail -10`'
    else:
        label = 'TODAY — GEAUGA + PORTAGE COUNTY'
        note = 'Run now if cron missed: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Geauga`'

    msg = (
        f'📍 *Geauga + Portage County Pull — {label} (July 13)*\n'
        f'>Week 29 rotation: Chardon, Painesville Township, Kent, Ravenna, Streetsboro, Aurora.\n'
        f'>Second cycle of peak season — these contacts are warm to summer exterior cleaning timing.\n'
        f'>After this: Week 30 = Cuyahoga 2nd pass (July 20), Week 31 = Lake 2nd pass (July 27).\n'
        f'>{note}\n'
        f'>Command: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Geauga`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'July 13 Geauga+Portage pull reminder posted — {label}')


def _check_july20_cuyahoga_2():
    """Fire July 14–20 countdown for Cuyahoga 2nd pass (Week 30, July 20 Monday).
    Week 30 % 6 = 0 → Cuyahoga in the rotation. Largest NE Ohio market — second pass
    catches contacts that didn't open Round 1, plus any new contacts pulled from new segments
    (school districts, car rentals, etc. added in Run 119). Peak season second half."""
    from datetime import date as _date_c2
    today = _date_c2.today()
    start = _date_c2(2026, 7, 14)
    end   = _date_c2(2026, 7, 20)
    if not (start <= today <= end):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.july20_cuyahoga_2_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    pull_date = _date_c2(2026, 7, 20)
    days_left = (pull_date - today).days
    if days_left > 0:
        label = f'{days_left} day{"s" if days_left != 1 else ""} away'
        note = 'Cron fires Mon July 20 at 7am. Verify: `cat logs/cron.log | tail -10`'
    else:
        label = 'TODAY — CUYAHOGA COUNTY 2ND PASS'
        note = 'Run now if cron missed: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Cuyahoga`'

    msg = (
        f'📍 *Cuyahoga County 2nd Pass — {label} (July 20)*\n'
        f'>Week 30 rotation: Cuyahoga — Cleveland, Lakewood, Parma, Strongsville, Berea, Westlake, Rocky River.\n'
        f'>Second pass: catches non-opens from June 8 + school districts now in active summer window.\n'
        f'>Highest-volume market — all 150+ commercial segments at max capacity.\n'
        f'>{note}\n'
        f'>Command: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Cuyahoga`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'July 20 Cuyahoga 2nd pass reminder posted — {label}')


def _check_july27_lake_2():
    """Fire July 21–27 countdown for Lake County 2nd pass (Week 31, July 27 Monday).
    Week 31 % 6 = 1 → Lake in the rotation. Mentor, Willoughby, Eastlake, Painesville,
    Wickliffe, Madison Township. Second pass + school districts in summer window."""
    from datetime import date as _date_l2
    today = _date_l2.today()
    start = _date_l2(2026, 7, 21)
    end   = _date_l2(2026, 7, 27)
    if not (start <= today <= end):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.july27_lake_2_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    pull_date = _date_l2(2026, 7, 27)
    days_left = (pull_date - today).days
    if days_left > 0:
        label = f'{days_left} day{"s" if days_left != 1 else ""} away'
        note = 'Cron fires Mon July 27 at 7am. Verify: `cat logs/cron.log | tail -10`'
    else:
        label = 'TODAY — LAKE COUNTY 2ND PASS'
        note = 'Run now if cron missed: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Lake`'

    msg = (
        f'📍 *Lake County 2nd Pass — {label} (July 27)*\n'
        f'>Week 31 rotation: Mentor, Willoughby-Eastlake, Wickliffe, Painesville, Madison Township.\n'
        f'>Second pass: Mentor Exempted Village Schools + Willoughby-Eastlake City Schools in summer window NOW.\n'
        f'>Marina + waterfront segment (Mentor Harbor, Mentor Lagoons) — late-July timing is peak.\n'
        f'>{note}\n'
        f'>Command: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Lake`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'July 27 Lake County 2nd pass reminder posted — {label}')


def _check_aug3_lorain_2():
    """Fire July 28–Aug 3 countdown for Lorain County 2nd pass (Week 32, Aug 3 Monday).
    Week 32 % 6 = 2 → Lorain. Elyria, Avon, North Ridgeville, Vermilion, Lorain city.
    Second pass — Avon corridor HOAs + Rt 83 industrial + Lorain Harbor marina.
    (Function name retained for sentinel compatibility; content corrected Run 137.)"""
    from datetime import date as _date_a3
    today = _date_a3.today()
    start = _date_a3(2026, 7, 28)
    end   = _date_a3(2026, 8, 3)
    if not (start <= today <= end):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.aug3_lorain_2_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    pull_date = _date_a3(2026, 8, 3)
    days_left = (pull_date - today).days
    label = f'{days_left} day{"s" if days_left != 1 else ""} away' if days_left > 0 else 'TODAY — LORAIN COUNTY 2ND PASS'
    note  = 'Cron fires Mon Aug 3 at 7am. Verify: `cat logs/cron.log | tail -10`' if days_left > 0 else \
            'Run now if cron missed: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Lorain`'

    msg = (
        f'📍 *Lorain County 2nd Pass — {label} (Aug 3)*\n'
        f'>Week 32 rotation: Elyria, Avon, North Ridgeville, Vermilion, Lorain city.\n'
        f'>Avon = fastest-growing NE Ohio suburb — 2nd pass hits new HOA subdivisions + Rt 83 industrial corridor.\n'
        f'>Lorain Harbor + Vermilion Lake Erie shoreline — late-summer marina dock cleanup pitch now active.\n'
        f'>{note}\n'
        f'>Command: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Lorain`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Aug 3 Lake County 2nd pass reminder posted — {label}')


def _check_aug10_summit_2():
    """Fire Aug 4–10 countdown for Summit County 2nd pass (Week 33, Aug 10 Monday).
    Week 33 % 6 = 3 → Summit. Akron, Fairlawn, Stow, Cuyahoga Falls, Hudson.
    Second pass — Firestone corridor golf + Akron Children's/Summa Health + Stan Hywet fall prep.
    (Function name retained for sentinel compatibility; content corrected Run 137.)"""
    from datetime import date as _date_a10
    today = _date_a10.today()
    start = _date_a10(2026, 8, 4)
    end   = _date_a10(2026, 8, 10)
    if not (start <= today <= end):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.aug10_summit_2_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    pull_date = _date_a10(2026, 8, 10)
    days_left = (pull_date - today).days
    label = f'{days_left} day{"s" if days_left != 1 else ""} away' if days_left > 0 else 'TODAY — SUMMIT COUNTY 2ND PASS'
    note  = 'Cron fires Mon Aug 10 at 7am. Verify: `cat logs/cron.log | tail -10`' if days_left > 0 else \
            'Run now if cron missed: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Summit`'

    msg = (
        f'📍 *Summit County 2nd Pass — {label} (Aug 10)*\n'
        f'>Week 33 rotation: Akron, Fairlawn, Stow, Cuyahoga Falls, Hudson.\n'
        f'>Firestone Country Club corridor + golf segment — fall clubhouse + cart area + parking lot cleanup pitch active.\n'
        f'>Akron Children\'s Hospital, Summa Health Akron City, Stan Hywet: fall maintenance budgets being set NOW.\n'
        f'>{note}\n'
        f'>Command: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Summit`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Aug 10 Lorain County 2nd pass reminder posted — {label}')


def _check_aug17_medina_3():
    """Fire Aug 11–17 countdown for Medina County 3rd pass (Week 34, Aug 17 Monday).
    Week 34 % 6 = 4 → Medina. Medina, Brunswick, Wadsworth, Seville.
    Third pass — Discount Drug Mart HQ + Smucker corridor + Medina City/Brunswick City school districts.
    (Function name retained for sentinel compatibility; content corrected Run 137.)"""
    from datetime import date as _date_a17
    today = _date_a17.today()
    start = _date_a17(2026, 8, 11)
    end   = _date_a17(2026, 8, 17)
    if not (start <= today <= end):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.aug17_medina_3_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    pull_date = _date_a17(2026, 8, 17)
    days_left = (pull_date - today).days
    label = f'{days_left} day{"s" if days_left != 1 else ""} away' if days_left > 0 else 'TODAY — MEDINA COUNTY 3RD PASS'
    note  = 'Cron fires Mon Aug 17 at 7am. Verify: `cat logs/cron.log | tail -10`' if days_left > 0 else \
            'Run now if cron missed: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Medina`'

    msg = (
        f'📍 *Medina County 3rd Pass — {label} (Aug 17)*\n'
        f'>Week 34 rotation: Medina, Brunswick, Wadsworth, Seville.\n'
        f'>Discount Drug Mart HQ (Medina) + J.M. Smucker corridor + Shiloh Foods (Lodi) — food processing segment peak.\n'
        f'>Medina City + Brunswick City school districts in summer window — B&G Directors booking fall contracts NOW.\n'
        f'>Shift pitch: "Lock in fall cleaning before October fills up."\n'
        f'>{note}\n'
        f'>Command: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Medina`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Aug 17 Summit County 3rd pass reminder posted — {label}')


def _check_aug24_geauga_portage_2():
    """Fire Aug 18–24 countdown for Geauga+Portage 3rd pass (Week 35, Aug 24 Monday).
    Week 35 % 6 = 5 → Geauga+Portage. Chardon, Chesterland, Bainbridge, Kent, Ravenna, Streetsboro, Aurora.
    Third pass — late-summer fall booking prep window; rural/suburban commercial + golf course segment.
    (Function name retained for sentinel compatibility — county corrected Run 135: was wrongly
     saying 'Medina County 3rd Pass' despite Week 35 = Geauga+Portage per ISO rotation.)"""
    from datetime import date as _date_a24
    today = _date_a24.today()
    start = _date_a24(2026, 8, 18)
    end   = _date_a24(2026, 8, 24)
    if not (start <= today <= end):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.aug24_geauga_portage_2_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    pull_date = _date_a24(2026, 8, 24)
    days_left = (pull_date - today).days
    label = f'{days_left} day{"s" if days_left != 1 else ""} away' if days_left > 0 else 'TODAY — GEAUGA + PORTAGE COUNTY 3RD PASS'
    note  = 'Cron fires Mon Aug 24 at 7am. Verify: `cat logs/cron.log | tail -10`' if days_left > 0 else \
            'Run now if cron missed: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Geauga`'

    msg = (
        f'📍 *Geauga + Portage County 3rd Pass — {label} (Aug 24)*\n'
        f'>Week 35: Chardon, Chesterland, Bainbridge, Kent, Ravenna, Streetsboro, Aurora. Fall angle fully active.\n'
        f'>Golf courses at end of peak season — book post-season clubhouse + cart area + parking lot clean.\n'
        f'>Cemeteries: October visitation peak approaching — book fall prep clean now.\n'
        f'>{note}\n'
        f'>Command: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Geauga`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Aug 24 Geauga+Portage County 3rd pass reminder posted — {label}')


def _check_aug31_cuyahoga_3():
    """Fire Aug 25–31 countdown for Cuyahoga County 3rd pass (Week 36, Aug 31 Monday).
    Week 36 % 6 = 0 → Cuyahoga. Cleveland, Parma, Lakewood, Strongsville, Beachwood, Rocky River.
    Third Cuyahoga pass — largest NE Ohio market final peak-season push; shift to fall closing angle.
    (Function name retained for sentinel compatibility; content corrected Run 137.)"""
    from datetime import date as _date_a31
    today = _date_a31.today()
    start = _date_a31(2026, 8, 25)
    end   = _date_a31(2026, 8, 31)
    if not (start <= today <= end):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.aug31_cuyahoga_3_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    pull_date = _date_a31(2026, 8, 31)
    days_left = (pull_date - today).days
    label = f'{days_left} day{"s" if days_left != 1 else ""} away' if days_left > 0 else 'TODAY — CUYAHOGA COUNTY 3RD PASS'
    note  = 'Cron fires Mon Aug 31 at 7am. Verify: `cat logs/cron.log | tail -10`' if days_left > 0 else \
            'Run now if cron missed: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Cuyahoga`'

    msg = (
        f'🏙️ *Cuyahoga County 3rd Pass — {label} (Aug 31) — FINAL PEAK SEASON PUSH*\n'
        f'>Week 36 rotation: Cleveland, Parma, Lakewood, Strongsville, Beachwood, Westlake, Rocky River.\n'
        f'>Largest NE Ohio market — 3rd pass catches every non-opener + summer turnover contacts.\n'
        f'>Schools back in session: facilities teams finalizing fall vendor lists NOW. Close before October fills.\n'
        f'>{note}\n'
        f'>Command: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Cuyahoga`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Aug 31 Geauga+Portage 3rd pass reminder posted — {label}')


def _check_sept7_lake_3():
    """Fire Sept 1–7 countdown for Lake County 3rd pass (Week 37, Sept 7 Monday).
    Week 37 % 6 = 1 → Lake. Mentor, Willoughby, Wickliffe, Painesville, Euclid, Eastlake.
    Third Lake pass — marina post-season cleanup window; school districts back in session + booking fall.
    (Function name retained for sentinel compatibility; content corrected Run 137.)"""
    from datetime import date as _date_s7
    today = _date_s7.today()
    start = _date_s7(2026, 9, 1)
    end   = _date_s7(2026, 9, 7)
    if not (start <= today <= end):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.sept7_lake_3_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    pull_date = _date_s7(2026, 9, 7)
    days_left = (pull_date - today).days
    label = f'{days_left} day{"s" if days_left != 1 else ""} away' if days_left > 0 else 'TODAY — LAKE COUNTY 3RD PASS'
    note  = 'Cron fires Mon Sept 7 at 7am. Verify: `cat logs/cron.log | tail -10`' if days_left > 0 else \
            'Run now if cron missed: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Lake`'

    msg = (
        f'⚓ *Lake County 3rd Pass — {label} (Sept 7) — MARINA POST-SEASON WINDOW*\n'
        f'>Week 37 rotation: Mentor, Willoughby, Wickliffe, Painesville, Euclid, Eastlake, Madison Township.\n'
        f'>Marina segment: Mentor Harbor, Sheffield Lake, Euclid shoreline — dock area + storage lot cleanup pitch.\n'
        f'>Mentor/Willoughby-Eastlake school districts back in session — facilities teams finalizing fall vendor lists.\n'
        f'>Pitch: "Lock in your fall cleaning before October. We\'re booking fast."\n'
        f'>{note}\n'
        f'>Command: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Lake`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Sept 7 Cuyahoga County 3rd pass reminder posted — {label}')


def _check_sept14_lorain_3():
    """Fire Sept 8–14 countdown for Lorain County 3rd pass (Week 38, Sept 14 Monday).
    Week 38 % 6 = 2 → Lorain. Elyria, Avon, North Ridgeville, Vermilion.
    Third pass — fall closing push; Avon HOAs locking in fall vendor lists; Lorain Harbor marina post-season.
    (Function name retained for sentinel compatibility; content corrected Run 137.)"""
    from datetime import date as _date_s14
    today = _date_s14.today()
    start = _date_s14(2026, 9, 8)
    end   = _date_s14(2026, 9, 14)
    if not (start <= today <= end):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.sept14_lorain_3_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    pull_date = _date_s14(2026, 9, 14)
    days_left = (pull_date - today).days
    label = f'{days_left} day{"s" if days_left != 1 else ""} away' if days_left > 0 else 'TODAY — LORAIN COUNTY 3RD PASS'
    note  = 'Cron fires Mon Sept 14 at 7am. Verify: `cat logs/cron.log | tail -10`' if days_left > 0 else \
            'Run now if cron missed: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Lorain`'

    msg = (
        f'📍 *Lorain County 3rd Pass — {label} (Sept 14)*\n'
        f'>Week 38 rotation: Elyria, Avon, North Ridgeville, Vermilion. Third pass — fall closing window.\n'
        f'>Avon HOA boards approving fall vendor lists NOW. Pitch: "Lock in before October fills."\n'
        f'>Lorain Harbor + Vermilion marina final post-season cleanup pitch.\n'
        f'>{note}\n'
        f'>Command: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Lorain`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Sept 14 Lake County 3rd pass reminder posted — {label}')


def _check_sept21_summit_3():
    """Fire Sept 15–21 countdown for Summit County 3rd pass (Week 39, Sept 21 Monday).
    Week 39 % 6 = 3 → Summit. Akron, Fairlawn, Stow, Cuyahoga Falls.
    Third Summit pass — industrial segment fall close; Akron corridor final push before freeze window.
    (Function name retained for sentinel compatibility; content corrected Run 137.)"""
    from datetime import date as _date_s21
    today = _date_s21.today()
    start = _date_s21(2026, 9, 15)
    end   = _date_s21(2026, 9, 21)
    if not (start <= today <= end):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.sept21_summit_3_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    pull_date = _date_s21(2026, 9, 21)
    days_left = (pull_date - today).days
    label = f'{days_left} day{"s" if days_left != 1 else ""} away' if days_left > 0 else 'TODAY — SUMMIT COUNTY 3RD PASS'
    note  = 'Cron fires Mon Sept 21 at 7am. Verify: `cat logs/cron.log | tail -10`' if days_left > 0 else \
            'Run now if cron missed: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Summit`'

    msg = (
        f'📍 *Summit County 3rd Pass — {label} (Sept 21) — INDUSTRIAL FALL CLOSE*\n'
        f'>Week 39 rotation: Akron, Fairlawn, Stow, Cuyahoga Falls.\n'
        f'>Industrial segment (manufacturing, distribution, towing) — last push before freeze window.\n'
        f'>Close pitch: "Last chance before the freeze. Book your fall clean this week — October fills fast."\n'
        f'>{note}\n'
        f'>Command: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Summit`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Sept 21 Lorain County 3rd pass reminder posted — {label}')


def _check_sept28_medina_4():
    """Fire Sept 22–28 countdown for Medina County 4th pass (Week 40, Sept 28 Monday).
    Week 40 % 6 = 4 → Medina. Medina, Brunswick, Wadsworth.
    Final Medina pass — last rotation before season close; shift fully to spring 2027 deposit mode after Oct 1.
    (Function name retained for sentinel compatibility; content corrected Run 137.)"""
    from datetime import date as _date_s28
    today = _date_s28.today()
    start = _date_s28(2026, 9, 22)
    end   = _date_s28(2026, 9, 28)
    if not (start <= today <= end):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.sept28_medina_4_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    pull_date = _date_s28(2026, 9, 28)
    days_left = (pull_date - today).days
    label = f'{days_left} day{"s" if days_left != 1 else ""} away' if days_left > 0 else 'TODAY — MEDINA COUNTY 4TH PASS'
    note  = 'Cron fires Mon Sept 28 at 7am. Verify: `cat logs/cron.log | tail -10`' if days_left > 0 else \
            'Run now if cron missed: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Medina`'

    msg = (
        f'📍 *Medina County 4th Pass — {label} (Sept 28) — LAST ROTATION BEFORE FREEZE WINDOW*\n'
        f'>Week 40 rotation: Medina, Brunswick, Wadsworth. Final Medina pass of the season.\n'
        f'>Medina commercial segment (Discount Drug Mart, food processing, golf courses) — final fall close.\n'
        f'>Close pitch: "Last chance before the freeze. Book your fall clean this week — October fills fast."\n'
        f'>After this rotation: season wraps. Relay shifts to October final push (Oct 1-15) then spring 2027 mode.\n'
        f'>{note}\n'
        f'>Command: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Medina`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Sept 28 Summit County 4th pass reminder posted — {label}')


def _check_fall_prep_reminder():
    """Fire every Monday Aug 3 – Sept 28.
    By August, the outreach message must shift from peak-season urgency to fall-booking urgency.
    'Lock in your fall clean before October fills up' is the closing pitch.
    Without this reminder, Bradley stays in summer mode too long and misses the fall window.
    Self-deactivates Oct 1."""
    from datetime import date as _date_fp
    today = _date_fp.today()
    start = _date_fp(2026, 8, 3)
    end   = _date_fp(2026, 9, 28)
    if not (start <= today <= end):
        return
    if today.weekday() != 0:  # Monday only
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.fall_prep_reminder_week'
    week_str = today.strftime('%Y-W%W')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == week_str:
        return

    msg = (
        '🍂 *Fall Booking — Shift the Pitch This Week*\n'
        '>August = the transition from "peak season urgency" to "fall booking window."\n'
        '>New closer for every quote call: "We\'re booking fall cleanings now — October fills fast.\n'
        '>   Lock in your date today and I\'ll block it for you."\n'
        '>Update the Mixmax sequence Touch 1 subject line: "Before your property sits dirty all winter…"\n'
        '>Past customer re-engagement text: "Hey [Name], time to schedule your fall cleaning before we fill up for October."\n'
        '>Annual Plan pitch gets easier in August — spring AND fall for one price, lock it in now.'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(week_str)
        except Exception:
            pass
        log(f'Fall prep weekly reminder posted — week {week_str}')


def _check_week2_facebook_ads():
    """Fire ONLY June 9 — 14 days after May 26 launch.
    Week 2 is the first window to make a meaningful scaling decision with real data.
    Day 7 (June 2) review was the diagnostic; June 9 is the action window: scale winners, kill losers.
    Without this, ads drift after the Day 7 check with no structured follow-through."""
    from datetime import date as _date_w2
    today = _date_w2.today()
    if today != _date_w2(2026, 6, 9):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.week2_facebook_ads_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    msg = (
        '📊 *Facebook Ads — Week 2 Scaling Action (June 9)*\n'
        '>14 days post-launch. You have real data. Time to act on it.\n'
        '>IF working (CPL < $25, leads coming in): bump budget 20% + test a new hook variant\n'
        '>IF mixed (some leads, high CPL): swap underperforming creative; do NOT touch targeting yet\n'
        '>IF nothing (0 leads, $0 spend): check campaign is active + form is submitting + lead notification email is set up\n'
        '>Week 2 scaling guide: `outputs/rick/week2_facebook_ads_scaling_guide_2026-05-26.md`\n'
        '>Ad week 1 revenue tracker: `outputs/rick/facebook_ad_week1_revenue_tracker_2026-05-26.md`\n'
        '>Key rule: never change budget + creative + targeting at the same time — one variable at a time.'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log('Week 2 Facebook ads scaling action reminder posted — June 9')


def _check_google_lsa_status_weekly():
    """Fire every Monday June 1 – Aug 31.
    Google Local Services Ads (Google Guaranteed) application may have been submitted May 22.
    Approval takes 7–14 days. Once approved, the badge appears above regular Google Ads.
    Weekly check ensures Bradley doesn't miss the approval window or forget to set up lead routing.
    Start date corrected from June 2 (Tuesday) to June 1 (Monday) — Run 129 bug fix."""
    from datetime import date as _date_lsa
    today = _date_lsa.today()
    start = _date_lsa(2026, 6, 1)
    end   = _date_lsa(2026, 8, 31)
    if not (start <= today <= end):
        return
    if today.weekday() != 0:  # Monday only
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.google_lsa_check_week'
    week_str = today.strftime('%Y-W%W')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == week_str:
        return

    lsa_approved = os.environ.get('GOOGLE_LSA_APPROVED', '').lower() == 'true'
    if lsa_approved:
        msg = (
            '🏅 *Google LSA — Weekly Lead Volume Check (Monday)*\n'
            '>Google Guaranteed is LIVE. Check your LSA dashboard for new leads this week.\n'
            '>LSA dashboard: ads.google.com/local-services-ads\n'
            '>Respond to new LSA leads within 5 min — Google tracks response time and it affects lead volume.\n'
            '>Response SOP: `outputs/rick/google_guaranteed_lead_response_sop_2026-05-22.md`\n'
            '>Log all LSA leads to pipeline_data.json (lead_source: "Google LSA").'
        )
    else:
        msg = (
            '🏅 *Google LSA — Weekly Status Check (Monday)*\n'
            '>Google Guaranteed application status: NOT CONFIRMED APPROVED.\n'
            '>If applied May 22: approval window was June 5–16. Check the status now.\n'
            '>Check here: ads.google.com/local-services-ads → "Status"\n'
            '>If APPROVED: add  GOOGLE_LSA_APPROVED=true  to .env and set up lead routing (SOP in `outputs/rick/`)\n'
            '>If PENDING: no action needed — just check again next Monday.\n'
            '>If NOT YET APPLIED: apply today — takes 20 min; puts you ABOVE regular Google Ads in search results.'
        )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(week_str)
        except Exception:
            pass
        log(f'Google LSA weekly status check posted — week {week_str}, approved={lsa_approved}')


def _check_neighbor_canvass_weekly():
    """Fire every Friday May 29 – Sept 25.
    After every active job, Bradley should knock on 3 neighboring doors.
    Tommy's script converts 20-30% of neighbors into same-day or next-day bookings.
    Zero ad spend, zero travel overhead — highest-ROI sales moment of the week.
    Weekly Friday reminder ensures the habit stays active all season."""
    from datetime import date as _date_nc
    today = _date_nc.today()
    start = _date_nc(2026, 5, 29)
    end   = _date_nc(2026, 9, 25)
    if not (start <= today <= end):
        return
    if today.weekday() != 4:  # Friday only
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.neighbor_canvass_week'
    week_str = today.strftime('%Y-W%W')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == week_str:
        return

    msg = (
        '🚪 *Neighbor Canvass — Weekly Reminder (Every Active Job)*\n'
        '>Before you leave EVERY job this week: knock on 3 neighboring doors.\n'
        '>"We\'re working on the house next door — want me to give you a quick quote while I\'m here?"\n'
        '>Same-day bookings convert at 20-30%. Zero extra drive time. Highest ROI moment in the business.\n'
        '>Script (all 3 door scenarios + same-day follow-up text): `outputs/tommy/neighbor_canvass_script_2026-05-26.md`\n'
        '>Log any booked neighbors in pipeline_data.json with lead_source="neighbor canvass".'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(week_str)
        except Exception:
            pass
        log(f'Neighbor canvass weekly reminder posted — week {week_str}')


def _check_early_cuyahoga_opportunity():
    """Fire May 28–June 7 — one-time window to run an EARLY Cuyahoga pull.
    150+ commercial segments won't get Cuyahoga contacts until the scheduled June 8 pull.
    Running Cuyahoga NOW gives those contacts extra days in the sequence before June 4 enrollment.
    This is additive — does NOT replace the June 8 rotation pull, it SUPPLEMENTS it.
    Self-deactivates June 8 (Cuyahoga IS the scheduled pull that day)."""
    from datetime import date as _date_ec
    today = _date_ec.today()
    start = _date_ec(2026, 5, 28)
    end   = _date_ec(2026, 6, 7)
    if not (start <= today <= end):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.early_cuyahoga_opportunity_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    days_to_june8 = (_date_ec(2026, 6, 8) - today).days
    msg = (
        f'🏙️ *Early Cuyahoga Pull Opportunity — {days_to_june8} Days Before Scheduled June 8 Pull*\n'
        f'>150+ commercial segments (hospital campuses, municipal facilities, DSO dental groups, YMCA branches,\n'
        f'>tire chains, movie theaters, bowling, pet boarding, dialysis, sports complexes, museums, food\n'
        f'>processing, airports, concert venues, craft breweries, dollar stores, auto parts, hardware,\n'
        f'>sports venues, cannabis dispensaries, blood/plasma centers, coin laundries, warehouse clubs,\n'
        f'>wireless retail, uniform services, optical centers, medical labs, tax prep offices,\n'
        f'>marine/boat dealers, ice cream chains, party/event rental,\n'
        f'>trampoline parks (Sky Zone/Urban Air/Scene75), moving companies (Two Men and a Truck),\n'
        f'>off-price retail (TJ Maxx/Marshalls/HomeGoods/Burlington), truck rental (U-Haul/Penske/Ryder),\n'
        f'>used car lots (CarMax/DriveTime), outdoor power equipment (STIHL/Husqvarna dealers),\n'
        f'>vocational & trade schools (CVCC/Ohio Technical College/Auburn CTE)) won\'t get\n'
        f'>Cuyahoga contacts until the June 8 scheduled pull.\n'
        f'>Running an EARLY pull today = {days_to_june8} extra days for those contacts BEFORE June 4 enrollment.\n'
        f'>✅ Title + org keyword batching active — all segments fully queried across multiple API batches.\n'
        f'>This is additive — won\'t interfere with the June 8 rotation pull.\n'
        f'>Shortcut: double-click `scripts/run_cuyahoga_both.command` in Finder (no typing required)\n'
        f'>Command: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py danny Cuyahoga`\n'
        f'>Guide: `outputs/vera/commercial_segments_early_pull_guide_2026-05-26.md`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Early Cuyahoga pull opportunity alert posted — {days_to_june8} days before June 8 scheduled pull')


def _check_spring_2027_early_booking():
    """Fire every Monday Oct 16, 2026 – March 31, 2027.
    After the Oct 15 final push, NE Ohio outdoor washing season closes.
    This is the 'Spring 2027 Early Booking Mode' — the off-season should generate spring deposits,
    not silence. Competitors who go dark in winter lose mindshare. Forest City can collect early
    deposits, pitch Annual Plans, and plan the 2027 ad campaign while competitors are dormant.
    Self-deactivates April 1, 2027."""
    from datetime import date as _date_sp
    today = _date_sp.today()
    start = _date_sp(2026, 10, 16)
    end   = _date_sp(2027, 3, 31)
    if not (start <= today <= end):
        return
    if today.weekday() != 0:  # Monday only
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.spring_2027_early_booking_week'
    week_str = today.strftime('%Y-W%W')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == week_str:
        return

    month = today.month
    if month >= 10:
        # October–December: collect early deposits + Annual Plan renewals
        msg = (
            '❄️ *Spring 2027 Early Booking — Off-Season Mode Active*\n'
            '>Season is closed. Competitors are dark. This is when you build next year\'s book.\n'
            '>This week\'s actions:\n'
            '>  1. Collect spring 2027 deposits from 2026 customers (10% discount for early booking)\n'
            '>  2. Annual Plan renewals — text customers: "Renew your annual plan now, lock in 2026 pricing"\n'
            '>  3. Commercial contacts who didn\'t convert: "We\'re booking spring 2027 contracts now. Slots fill fast."\n'
            '>Past customer text: "Hey [Name], Forest City here. Booking spring 2027 now. Want first pick of dates? $50 deposit holds your slot."\n'
            '>Goal: 20+ spring deposits by Jan 1 = guaranteed spring revenue before the season starts.'
        )
    else:
        # January–March: push harder on spring bookings, start ad campaign planning
        msg = (
            '🌱 *Spring 2027 Early Booking — Final Push Before Season Restarts*\n'
            '>Spring is approaching. Time to convert off-season interest into booked jobs.\n'
            '>This week\'s actions:\n'
            '>  1. Follow up on any outstanding early-booking deposits from October–December outreach\n'
            '>  2. Plan 2027 ad campaigns — review what worked in 2026 (CPL, best creative, peak dates)\n'
            '>  3. Re-engage commercial contacts from 2026 sequences who went cold — new outreach angle: "2027 spring pricing"\n'
            '>  4. Check if Google LSA is still active — if not, re-apply before April ad spend\n'
            '>Launch calendar: target ads-on by April 1 to capture the first warm weekends.'
        )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(week_str)
        except Exception:
            pass
        log(f'Spring 2027 early booking reminder posted — week {week_str}')


def _check_october_final_push():
    """Fire Oct 1–15 — last bookings before the NE Ohio freeze window closes.
    NE Ohio typically drops below 40°F overnight around Oct 20–Nov 1.
    This is the final 2-week window to book exterior cleaning before properties sit dirty all winter.
    Urgency pitch: 'Lock in your date this week — October fills fast and we stop taking new bookings Nov 1.'
    Without this reminder, Bradley stays in peak-season mode too long and misses the fall close window."""
    from datetime import date as _date_oct
    today = _date_oct.today()
    start = _date_oct(2026, 10, 1)
    end   = _date_oct(2026, 10, 15)
    if not (start <= today <= end):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.october_final_push_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    days_left_in_window = (end - today).days
    msg = (
        f'❄️ *October Final Push — {days_left_in_window} days left in booking window*\n'
        '>NE Ohio freeze window: temperatures drop below cleaning threshold around Oct 20.\n'
        '>THIS WEEK: past customer blast — "Time for your fall cleaning before the freeze. We\'re booking fast."\n'
        '>Close on EVERY open quote: "October is almost full — want me to block a date for you today?"\n'
        '>Annual Plan pitch: spring + fall for one price — lock both dates in now while you have them.\n'
        '>After Oct 15: shift to "Spring 2027 Early Booking" mode. Start collecting spring deposits.\n'
        '>Past customer text script: `outputs/tommy/past_customer_june_text_scripts_2026-05-26.md` (adapt for fall urgency)\n'
        '>Annual plan pitch: `outputs/tommy/annual_plan_pitch_script_2026-05-26.md`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'October final push reminder posted — {days_left_in_window} days left in window')


def _check_weekly_booking_velocity():
    """Fire every Friday June 1 – Sept 25.
    During peak season, Bradley needs to check weekly booking velocity.
    Workiz is the ground truth — are enough jobs being booked to hit monthly targets?
    Without this, ads spend and outreach runs but nobody checks whether efforts
    are converting into booked revenue. Self-deactivates Sept 26."""
    from datetime import date as _date_bv
    today = _date_bv.today()
    start = _date_bv(2026, 6, 1)
    end   = _date_bv(2026, 9, 25)
    if not (start <= today <= end):
        return
    if today.weekday() != 4:  # Friday only
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.booking_velocity_week'
    week_str = today.strftime('%Y-W%W')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == week_str:
        return

    msg = (
        '📈 *Weekly Booking Velocity Check — End of Week*\n'
        '>5 minutes in Workiz tells you if this week\'s ads + outreach are converting.\n'
        '>Check:\n'
        '>  1. Jobs booked this week → are you on pace for monthly goal?\n'
        '>  2. Revenue booked this week → residential vs. commercial split?\n'
        '>  3. Outstanding quotes → follow up on any estimate sitting > 3 days\n'
        '>  4. Lead source → which source (ad, outreach reply, past customer, neighbor canvass) drove the most?\n'
        '>Run Workiz report: `cd /Users/bradleyneal/forestcity && python3 workers/workiz_report.py daily`\n'
        '>Target: 8–12 jobs/week in peak season = $4,800–$8,400/week at $600 avg job value.\n'
        '>Outstanding quote follow-up: `outputs/tommy/quote_followup_sequence_2026-05-21.md`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(week_str)
        except Exception:
            pass
        log(f'Weekly booking velocity check reminder posted — week {week_str}')


def _check_gbp_weekly_post():
    """Fire every Monday May 26 – Sept 30.
    Google Business Profile posts keep Forest City active in Maps rankings during peak season.
    Tommy wrote a June GBP content calendar (june_gbp_content_calendar_2026-05-24.md).
    Most NE Ohio power washing competitors never post to GBP — weekly posting is free organic lead gen.
    Weekly Monday reminder keeps the GBP habit active all season. Self-deactivates Oct 1."""
    from datetime import date as _date_gbp
    today = _date_gbp.today()
    start = _date_gbp(2026, 5, 26)
    end   = _date_gbp(2026, 9, 30)
    if not (start <= today <= end):
        return
    if today.weekday() != 0:  # Monday only
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.gbp_weekly_post_week'
    week_str = today.strftime('%Y-W%W')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == week_str:
        return

    msg = (
        '📍 *GBP Post Due — Google Business Profile (Monday)*\n'
        '>One GBP post/week keeps Forest City active in Maps rankings during peak season.\n'
        '>Competitors go silent all summer — an active GBP stands out in local search.\n'
        '>June content calendar (pre-written posts ready to copy): `outputs/vera/june_gbp_content_calendar_2026-05-24.md`\n'
        '>Best-performing hook: before/after with location tag ("Just finished this driveway in [City] — result speaks for itself.")\n'
        '>Post types that drive leads: before/after photo, seasonal availability notice, job spotlight, 5-star review share.\n'
        '>5 minutes: Google Business Profile Manager → Posts → Add Update → publish.'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(week_str)
        except Exception:
            pass
        log(f'GBP weekly post reminder posted — week {week_str}')


def _check_june2_medina_verification():
    """Fire ONLY June 2 — verify that the June 1 Medina pull actually ran.
    The Monday cron fires June 1 at 7am. If it ran, .danny_last_pull_date reads '2026-06-01'.
    If cron failed or skipped, June 4 enrollment is missing Medina leads — escalate immediately.
    One-time, self-deactivating."""
    from datetime import date as _date_mv
    today = _date_mv.today()
    if today != _date_mv(2026, 6, 2):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.june2_medina_verify_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    danny_sentinel = BASE_DIR / 'outputs' / 'vera' / '.danny_last_pull_date'
    carla_sentinel  = BASE_DIR / 'outputs' / 'vera' / '.carla_last_pull_date'
    danny_ran = False
    carla_ran = False
    try:
        if danny_sentinel.exists():
            danny_ran = danny_sentinel.read_text().strip() == '2026-06-01'
    except Exception:
        pass
    try:
        if carla_sentinel.exists():
            carla_ran = carla_sentinel.read_text().strip() == '2026-06-01'
    except Exception:
        pass

    if danny_ran and carla_ran:
        msg = (
            '✅ *Medina Pull Verification — June 1 Pull CONFIRMED (Danny + Carla)*\n'
            '>Both Danny and Carla ran their Medina pull June 1. New leads are in the pipeline.\n'
            '>Run Nina\'s daily report to surface hot leads: `cd /Users/bradleyneal/forestcity && python3 workers/nina_report.py daily`\n'
            '>June 4 enrollment is 2 days away — Medina leads are ready to enroll.'
        )
    elif danny_ran and not carla_ran:
        msg = (
            '⚠️ *Medina Pull Verification — Danny Confirmed, Carla DID NOT RUN*\n'
            '>Danny\'s Medina pull ran June 1 ✅. Carla\'s referral partner pull did NOT run ❌.\n'
            '>Run Carla\'s Medina pull now (2 min): `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py carla Medina`\n'
            '>June 4 enrollment needs both Danny + Carla Medina leads for full coverage.'
        )
    else:
        msg = (
            '🚨 *Medina Pull Verification — June 1 Pull DID NOT RUN*\n'
            '>The Monday cron pull for June 1 did NOT run (or ran and found 0 leads).\n'
            '>June 4 enrollment is in 2 DAYS and is missing the Medina County lead batch.\n'
            '>Run it NOW — 10 min unattended: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Medina`\n'
            '>Or double-click: `scripts/run_medina_both.command` in Finder.\n'
            '>Check cron status: `cat logs/cron.log | tail -20` — verify cron is running.'
        )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'June 2 Medina pull verification posted — danny_ran={danny_ran}, carla_ran={carla_ran}')


def _check_post_june8_commercial_monitoring():
    """Fire June 9–11: 3-day monitoring window immediately after the June 8 Cuyahoga pull.
    Relay coverage gap: _check_june8_geauga_portage() ends June 8;
    _check_post_june11_monitoring() starts June 12. June 9-11 was completely dark.
    NOTE: The June 15 Lake County pull (marina corridor) fires next week."""
    from datetime import date as _date_jc
    today = _date_jc.today()
    start = _date_jc(2026, 6, 9)
    end   = _date_jc(2026, 6, 11)
    if not (start <= today <= end):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.post_june8_commercial_monitor_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    day_num = (today - start).days + 1  # June 9 = Day 1 post-Cuyahoga pull
    title_batch_note = (
        '> ✅ Title batching active (Run 132): June 8 pull used 4 batches of 50 titles instead of 1 massive\n'
        '>    call. Check the output file — you should see contacts with titles like "YMCA Director",\n'
        '>    "Dialysis District Manager", "Food Plant Manager", "Airport Facilities Manager", "Museum Director".\n'
        '>    If those titles are ABSENT, Apollo is still capping — notify Vera immediately.\n'
    ) if day_num == 1 else ''
    msg = (
        f'🏙️ *Post-Cuyahoga Pull — Day {day_num} Commercial Enrollment Watch (June {today.day})*\n'
        f'>The June 8 Cuyahoga pull enrolled the largest commercial batch of the season (150+ segments).\n'
        f'>First opens expected today — DSO district managers, hospital FMs, government facilities contacts.\n'
        f'{title_batch_note}'
        f'>Run Nina\'s hot leads report: `cd /Users/bradleyneal/forestcity && python3 workers/nina_report.py daily`\n'
        f'>Commercial replies need segment-specific openers — NOT the same "Thanks for opening!" as PM sequence.\n'
        f'>DSO/hospital/government contact replied? Book a site walk immediately — these are annual contracts.\n'
        f'>Hot lead (2+ opens, no reply): connect on LinkedIn TODAY — message: "saw you opened our email about cleaning your facilities"'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Post-June 8 commercial enrollment monitoring posted — Day {day_num}')


def _check_fathers_day_blast():
    """Fire June 15–20: remind Bradley to run a Father's Day residential re-engagement blast.
    Father's Day = June 21. Past residential customers with driveways/patios/siding = natural June recipients.
    Fastest non-ad revenue during the post-June-8 lull before sequences warm up.
    Tommy wrote the June residential blast guide (past_customer_june_blast_2026-05-27.md) —
    adapt those scripts for Father's Day angle. Self-deactivates June 21."""
    from datetime import date as _date_fd
    today = _date_fd.today()
    start = _date_fd(2026, 6, 15)
    end   = _date_fd(2026, 6, 20)
    if not (start <= today <= end):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.fathers_day_blast_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    days_left = (_date_fd(2026, 6, 21) - today).days
    label = 'TOMORROW — LAST WINDOW' if days_left == 1 else f'{days_left} days until Father\'s Day'

    msg = (
        f'👨 *Father\'s Day Residential Blast — {label} (June {today.day})*\n'
        f'>Father\'s Day = June 21. Homeowners whose dads care about curb appeal are a perfect June re-engage.\n'
        f'>Past residential customers who booked in 2024–2025 and haven\'t returned = prime list.\n'
        f'>Text angle: "Get Dad\'s driveway, patio, and house washed before the weekend — one call, one visit."\n'
        f'>Or: "Father\'s Day gift that actually gets used: a clean driveway. We have openings this week."\n'
        f'>Open Tommy\'s past customer scripts: `outputs/tommy/past_customer_june_blast_2026-05-27.md`\n'
        f'>Look up 2024–2025 residential jobs in Workiz → pull phone numbers → 15 min of texts = $1,000–$3,000.\n'
        f'>Commercial sequences are sending — residential texting fills the booking calendar while they warm up.'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f"Father's Day residential blast reminder posted — {label}")


def _check_oct5_geauga_portage_4():
    """Fire Oct 1–5 countdown for Geauga+Portage 4th pass (Week 41, Oct 5 Monday).
    Week 41 % 6 = 5 → Geauga+Portage. Chardon, Chesterland, Kent, Ravenna, Streetsboro, Aurora.
    GAP FIX (Run 149): _check_sept28_medina_4() ends Sept 28; Oct 5 had zero relay coverage.
    This is the FINAL county rotation of 2026 season per Carla's calendar (Week 41 = end of season)."""
    from datetime import date as _date_o5
    today = _date_o5.today()
    start = _date_o5(2026, 10, 1)
    end   = _date_o5(2026, 10, 5)
    if not (start <= today <= end):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.oct5_geauga_portage_4_sent_date'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    pull_date = _date_o5(2026, 10, 5)
    days_left = (pull_date - today).days
    label = f'{days_left} day{"s" if days_left != 1 else ""} away' if days_left > 0 else 'TODAY — GEAUGA + PORTAGE FINAL PASS'
    note  = 'Cron fires Mon Oct 5 at 7am. Verify: `cat logs/cron.log | tail -10`' if days_left > 0 else \
            'Run now if cron missed: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Geauga`'

    msg = (
        f'📍 *Geauga + Portage County Final Pass — {label} (Oct 5) — LAST ROTATION OF 2026*\n'
        f'>Week 41: Chardon, Chesterland, Kent, Ravenna, Streetsboro, Aurora. FINAL county rotation of peak season.\n'
        f'>Last chance to close Geauga+Portage contacts before the NE Ohio freeze window (Oct 15–20).\n'
        f'>Close pitch: "Book your fall clean this week — October fills fast and we stop taking new bookings Nov 1."\n'
        f'>After Oct 5: cron rotation ends for the season. Relay shifts to October final push (Oct 1–15) + spring 2027 mode.\n'
        f'>{note}\n'
        f'>Command: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Geauga`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Oct 5 Geauga+Portage 4th pass (final season rotation) reminder posted — {label}')


def _check_june9_cuyahoga_verification():
    """Fire ONLY on June 9 — the day after the June 8 Cuyahoga pull (biggest pull of the year).
    Reads Danny + Carla sentinel files (.danny_last_pull_date / .carla_last_pull_date) to confirm
    the pull actually ran. Posts confirmed success OR an emergency ALERT if it was silently missed.
    June 8 = 150+ segments, largest single-day commercial pull of peak season. One-time, self-deactivating.
    Proposed Run 144, implemented Run 146."""
    from datetime import date as _date_j9
    today = _date_j9.today()
    if today != _date_j9(2026, 6, 9):
        return

    alert_sentinel = BASE_DIR / 'outputs' / 'vera' / '.june9_cuyahoga_verification_sent'
    today_str = today.strftime('%Y-%m-%d')
    if alert_sentinel.exists() and alert_sentinel.read_text().strip() == today_str:
        return

    danny_sentinel = BASE_DIR / 'outputs' / 'vera' / '.danny_last_pull_date'
    carla_sentinel  = BASE_DIR / 'outputs' / 'vera' / '.carla_last_pull_date'
    june8_str = '2026-06-08'

    danny_ran = danny_sentinel.exists() and danny_sentinel.read_text().strip() == june8_str
    carla_ran  = carla_sentinel.exists() and carla_sentinel.read_text().strip() == june8_str

    if danny_ran and carla_ran:
        msg = (
            '✅ *Cuyahoga Pull Confirmed — June 8 Ran Successfully (Danny + Carla)*\n'
            '>Danny sentinel: June 8 ✓ | Carla sentinel: June 8 ✓\n'
            '>All 150+ commercial segments enrolled. First opens expected June 11–13 (Touch 1 Day 0 → opens by Day 3).\n'
            '>Action: Run Nina\'s daily report Monday June 9 morning to surface hot leads before they cool.\n'
            '>`cd /Users/bradleyneal/forestcity && python3 workers/nina_report.py daily`\n'
            '>DSO district manager / hospital FM / government contact replied? Book a site walk immediately — annual contract.'
        )
    elif danny_ran:
        msg = (
            '⚠️ *Cuyahoga Pull — Danny Ran, Carla NOT Confirmed (June 8)*\n'
            '>Danny sentinel: June 8 ✓ | Carla sentinel: NOT June 8\n'
            '>Carla\'s referral partner pull (realtors, landscapers, contractors — Cuyahoga) may not have run.\n'
            '>Run now: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py carla Cuyahoga`\n'
            '>Or double-click: `scripts/run_cuyahoga_both.command` — Danny deduplicates, Carla adds fresh contacts.'
        )
    else:
        msg = (
            '🚨 *ALERT — June 8 Cuyahoga Pull Not Confirmed*\n'
            '>Danny sentinel NOT dated June 8. Largest commercial pull of the year may have been silently missed.\n'
            '>RUN NOW (15–20 min): `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Cuyahoga`\n'
            '>Or double-click: `scripts/run_cuyahoga_both.command` in Finder — no typing required.\n'
            '>150+ commercial segments. Missing this = no hospital/DSO/government/museum contacts for the entire season.\n'
            '>Check cron first: `cat logs/cron.log | tail -30` — if cron ran but sentinel is absent, re-run anyway.'
        )

    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log('June 9 Cuyahoga pull verification check posted')


def _main_body():
    # Always check staleness (runs even if no new Vera commits)
    _check_danny_staleness()
    _check_carla_staleness()
    _check_nina_staleness()
    _check_workiz_staleness()
    _check_instantly_paused()
    _check_summit_deadline()
    _check_gas_station_pending()
    _check_ad_lead_log_reminder()
    _check_medina_reminder()
    _check_day7_ads_review()
    _check_june4_enrollment_countdown()
    _check_june4_enrollment_day()
    _check_day3_ads_check()
    _check_post_june4_monitoring()
    _check_wave2_contractor_blitz()
    _check_past_customer_blast()
    _check_ad_lead_day5_escalation()
    _check_wave2_day3_followup()
    _check_june8_geauga_portage()
    _check_june22_lake_county()
    _check_june15_cuyahoga()
    _check_june29_lorain()
    _check_post_june11_monitoring()
    _check_review_request_reminder()
    _check_pipeline_overdue_contacts()
    _check_wave2_day7_followup()
    _check_instagram_reminder()
    _check_annual_plan_pitch_reminder()
    _check_fleet_sequence_pending()
    _check_july6_medina()
    _check_july13_geauga_portage()
    _check_july20_cuyahoga_2()
    _check_july27_lake_2()
    _check_aug3_lorain_2()
    _check_aug10_summit_2()
    _check_aug17_medina_3()
    _check_aug24_geauga_portage_2()
    _check_aug31_cuyahoga_3()
    _check_sept7_lake_3()
    _check_sept14_lorain_3()
    _check_sept21_summit_3()
    _check_sept28_medina_4()
    _check_oct5_geauga_portage_4()
    _check_fall_prep_reminder()
    _check_week2_facebook_ads()
    _check_google_lsa_status_weekly()
    _check_neighbor_canvass_weekly()
    _check_weekly_booking_velocity()
    _check_gbp_weekly_post()
    _check_october_final_push()
    _check_early_cuyahoga_opportunity()
    _check_spring_2027_early_booking()
    _check_june2_medina_verification()
    _check_post_june8_commercial_monitoring()
    _check_fathers_day_blast()
    _check_june9_cuyahoga_verification()

    # Fetch first so origin/main is current before flush checks origin/main..HEAD
    git(['fetch', 'origin'])

    # Flush unpushed commits before pulling — prevents cleared-file rebase clobbering new messages
    _flush_unpushed_commits()

    # Pull latest
    git(['pull', '--rebase', 'origin', 'main'])

    # Get last known commit
    last_commit = STATE_FILE.read_text().strip() if STATE_FILE.exists() else ''

    # Get latest commit SHA
    result = git(['log', 'origin/main', '-100', '--format=%H|%an|%s'])
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
