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
    After May 31 Summit doesn't run until July 6 (Medina→Geauga+Portage→Cuyahoga rotation).
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
    msg = (
        f'{urgency_emoji} *Summit County Pull — {days_label} (Deadline May 31)*\n'
        f'>Miss this window = no Summit leads until July 6 (next time it comes up in rotation).\n'
        f'>All new commercial segments (restaurants, banks, gyms, medical offices) miss peak season.\n'
        f'>Command (6 min, unattended): `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py danny Summit`\n'
        f'>Or double-click: scripts/run_summit_pull.command in Finder.'
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
    if not pipeline_f.exists():
        return
    try:
        import json as _json
        pd = _json.loads(pipeline_f.read_text())
        gas_contacts = [
            c for c in pd.get('manual_contacts', [])
            if c.get('lead_type') == 'gas_station' or c.get('_lead_type') == 'gas_station'
        ]
    except Exception:
        return

    if not gas_contacts:
        return

    msg = (
        f'⛽ *Gas Station Sequence Still PENDING — {len(gas_contacts)} contacts waiting*\n'
        f'>These {len(gas_contacts)} contacts cannot be enrolled until you create the Mixmax sequence (30 min).\n'
        f'>Setup guide: `outputs/danny/gas_station_sequence_create_now_2026-05-27.md`\n'
        f'>Or: Mixmax → Sequences → New → paste ID into `integrations/mixmax.py` line 54.'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Gas station PENDING alert posted — {len(gas_contacts)} contacts waiting')


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
    """Fire Medina County pull reminder May 30–June 4 (pull due June 1, needed for June 4 enrollment)."""
    from datetime import date as _date_m
    today = _date_m.today()
    start = _date_m(2026, 5, 30)
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
    start = _date_j4(2026, 6, 2)
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
    """Fire June 4–8 countdown for the Geauga + Portage County pull (Week 23, June 8 Monday).
    Geauga + Portage = Chardon, Chesterland, Kent, Ravenna — smaller market but
    funeral homes, self-storage, HOA management firms, and rural commercial properties.
    Cron handles this automatically, but a reminder surfaces it if cron drifts."""
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
        note = 'Cron will fire automatically Mon 7am if running. Verify cron is live: `cat logs/cron.log | tail -10`'
    else:
        label = 'TODAY'
        note = 'Run now if cron missed it: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Geauga+Portage`'

    msg = (
        f'📍 *Geauga + Portage County Pull — {label} (June 8)*\n'
        f'>Week 23 county rotation: Chardon, Chesterland, Kent, Ravenna.\n'
        f'>Smaller market (~15–25 leads) but includes: funeral homes, self-storage, HOA mgmt firms, rural commercial.\n'
        f'>{note}\n'
        f'>If cron is off: `python3 workers/lead_pipeline.py both Geauga+Portage`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Geauga + Portage County pull reminder posted — {label}')


def _check_june22_lake_county():
    """Fire June 17–22 countdown for the Lake County pull (Week 25, June 22 Monday).
    Lake County = Mentor, Willoughby, Painesville — AND the Lake Erie shoreline.
    This is the MARINA county. Mentor Harbor, Sheffield Lake, Euclid marina, Lorain Harbor.
    Pre-season is gone but summer maintenance window is open — contact marina managers NOW."""
    from datetime import date as _date_lk
    today = _date_lk.today()
    start = _date_lk(2026, 6, 17)
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
        note = f'Staging now — cron fires June 22 Monday 7am.'
    else:
        label = 'TODAY — LAKE ERIE MARINA PULL'
        note = 'Run now: `python3 workers/lead_pipeline.py both Lake` or double-click Lake shortcut if it exists.'

    msg = (
        f'⚓ *Lake County Pull — {label} (June 22) — MARINA SEGMENT*\n'
        f'>Lake County is the marina/waterfront county: Mentor Harbor, Sheffield Lake, Euclid shoreline, Bratenahl.\n'
        f'>Marina managers need mid-season cleaning (June–July) for dock areas, fuel station concrete, boat ramp.\n'
        f'>Also in this county: hotel chains (Mentor/Willoughby corridor), senior living, retail PM firms.\n'
        f'>{note}\n'
        f'>Command: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Lake`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Lake County pull reminder posted — {label}')


def _check_june15_cuyahoga():
    """Fire June 10–15 countdown for the Cuyahoga County pull (Week 24, June 15 Monday).
    Cuyahoga is the LARGEST market — Cleveland, Parma, Lakewood, Strongsville, Beachwood.
    All new commercial segments (restaurants, banks, urgent care, fitness, hotels) fire here
    at maximum volume. Never miss the Cuyahoga window."""
    from datetime import date as _date_cy
    today = _date_cy.today()
    start = _date_cy(2026, 6, 10)
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
        note = 'Cron fires Mon 7am if running. Verify: `cat logs/cron.log | tail -10`'
    else:
        label = 'TODAY — CUYAHOGA (LARGEST COUNTY)'
        note = 'Run now if cron missed: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Cuyahoga`'

    msg = (
        f'🏙️ *Cuyahoga County Pull — {label} (June 15) — BIGGEST MARKET*\n'
        f'>Cuyahoga = Cleveland, Parma, Lakewood, Strongsville, Beachwood. Highest lead volume of all 6 counties.\n'
        f'>All commercial segments fire here at max volume: restaurants, banks, urgent care, hotels, fitness, grocery.\n'
        f'>{note}\n'
        f'>Command: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Cuyahoga`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Cuyahoga June 15 pull reminder posted — {label}')


def _check_june29_lorain():
    """Fire June 24–29 countdown for the Lorain County pull (Week 26, June 29 Monday).
    Lorain = Elyria, Avon, North Ridgeville — strong industrial + HOA corridor.
    Avon is one of the fastest-growing NE Ohio suburbs — high HOA density + new commercial."""
    from datetime import date as _date_lo
    today = _date_lo.today()
    start = _date_lo(2026, 6, 24)
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
        label = 'TODAY — LORAIN COUNTY'
        note = 'Run now if cron missed: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Lorain`'

    msg = (
        f'📍 *Lorain County Pull — {label} (June 29)*\n'
        f'>Lorain = Elyria, Avon, North Ridgeville. Avon is one of NE Ohio\'s fastest-growing suburbs.\n'
        f'>High HOA density in Avon subdivisions + strong industrial corridor along Rt 83 (self-storage, auto body, distribution).\n'
        f'>{note}\n'
        f'>Command: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Lorain`'
    )
    if post_slack(msg):
        alert_sentinel.parent.mkdir(exist_ok=True)
        try:
            alert_sentinel.write_text(today_str)
        except Exception:
            pass
        log(f'Lorain June 29 pull reminder posted — {label}')


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
    _check_nina_staleness()
    _check_workiz_staleness()
    _check_instantly_paused()
    _check_summit_deadline()
    _check_gas_station_pending()
    _check_ad_lead_log_reminder()
    _check_medina_reminder()
    _check_day7_ads_review()
    _check_june4_enrollment_countdown()
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
