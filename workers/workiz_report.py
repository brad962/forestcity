#!/usr/bin/env python3
"""
Workiz Report — Forest City Power Washing
Pulls jobs from Workiz filtered to JobType = "Power Washing"
Reports revenue, job count, status breakdown, and upcoming jobs.
"""

import os
import json
import datetime
import urllib.request
try:
    import requests as _requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False
from dotenv import load_dotenv

# Load env
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

WORKIZ_TOKEN = os.environ.get('WORKIZ_API_TOKEN', 'api_rays65iotbi9jpu28uden04mmv3n9rzu')
WORKIZ_SECRET = os.environ.get('WORKIZ_API_SECRET', 'sec_252658762260613604129161295')
SLACK_WEBHOOK = os.environ.get('SLACK_WEBHOOK_OFFICE', '')

BASE_URL = f"https://api.workiz.com/api/v1/{WORKIZ_TOKEN}"
JOB_TYPE_FILTER = "Power Washing"
# Accept common casing/naming variations from Workiz
JOB_TYPE_VARIANTS = {
    'power washing', 'power wash', 'powerwashing', 'powerwash',
    'pressure washing', 'pressure wash', 'pressurewashing',
    'exterior cleaning', 'house washing', 'soft wash', 'softwash',
}


def _is_power_washing_job(job_type: str) -> bool:
    return job_type.strip().lower() in JOB_TYPE_VARIANTS


def fetch_all_jobs():
    """Pull all jobs from Workiz, filter to Power Washing only."""
    url = f"{BASE_URL}/job/all/"
    headers = {"Authorization": WORKIZ_SECRET}
    try:
        if HAS_REQUESTS:
            resp = _requests.get(url, headers=headers, timeout=15)
            resp.raise_for_status()
            data = resp.json()
        else:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as r:
                data = json.loads(r.read())
    except Exception as e:
        print(f"Workiz API error: {e}")
        return []

    all_jobs = data.get('data', [])
    pw_jobs = [j for j in all_jobs if _is_power_washing_job(j.get('JobType', ''))]
    print(f"  Workiz: {len(all_jobs)} total jobs, {len(pw_jobs)} power washing jobs")
    if all_jobs and not pw_jobs:
        types_seen = {j.get('JobType', '') for j in all_jobs[:20]}
        print(f"  JobType values seen (first 20 jobs): {types_seen}")
    return pw_jobs


def generate_report(mode='daily'):
    """Generate daily or weekly Power Washing job report."""
    today = datetime.date.today()
    jobs = fetch_all_jobs()

    if not jobs:
        return {
            'report': f"# Workiz — Power Washing Jobs\n**Date:** {today}\n\nNo Power Washing jobs found in Workiz yet. Jobs will appear here once they are entered with JobType = 'Power Washing'.\n",
            'jobs': [],
            'summary': 'No Power Washing jobs found.'
        }

    # Status breakdown
    status_counts = {}
    for j in jobs:
        s = j.get('Status', 'Unknown')
        status_counts[s] = status_counts.get(s, 0) + 1

    # Revenue
    total_revenue = sum(j.get('JobTotalPrice', 0) for j in jobs)
    total_due = sum(j.get('JobAmountDue', 0) for j in jobs)
    paid = total_revenue - total_due

    # Upcoming jobs (next 30 days)
    upcoming = []
    for j in jobs:
        try:
            job_dt = datetime.datetime.strptime(j['JobDateTime'], '%Y-%m-%d %H:%M:%S').date()
            days_out = (job_dt - today).days
            if 0 <= days_out <= 30:
                upcoming.append((days_out, j))
        except Exception:
            pass
    upcoming.sort(key=lambda x: x[0])

    # Recent completions (last 7 days)
    recent = []
    for j in jobs:
        if j.get('Status', '').lower() in ['done', 'completed', 'paid']:
            try:
                job_dt = datetime.datetime.strptime(j['JobDateTime'], '%Y-%m-%d %H:%M:%S').date()
                if (today - job_dt).days <= 7:
                    recent.append(j)
            except Exception:
                pass

    # Build report
    lines = [
        f"# Workiz — Power Washing Jobs Report",
        f"**Date:** {today}  |  **Mode:** {mode.title()}",
        f"",
        f"## Summary",
        f"- **Total Power Washing Jobs:** {len(jobs)}",
        f"- **Total Job Value:** ${total_revenue:,.2f}",
        f"- **Collected:** ${paid:,.2f}",
        f"- **Outstanding:** ${total_due:,.2f}",
        f"",
        f"## Status Breakdown",
    ]
    for status, count in sorted(status_counts.items(), key=lambda x: -x[1]):
        lines.append(f"- {status}: {count} job{'s' if count != 1 else ''}")

    if upcoming:
        lines += ["", f"## Upcoming Jobs (Next 30 Days)", ""]
        for days_out, j in upcoming:
            name = f"{j.get('FirstName','')} {j.get('LastName','')}".strip() or j.get('Company', 'Unknown')
            addr = j.get('LocationKey', j.get('Address', ''))
            price = j.get('JobTotalPrice', 0)
            due = j.get('JobAmountDue', 0)
            dt = j.get('JobDateTime', '')[:10]
            tag_str = ', '.join(j.get('Tags', [])) if j.get('Tags') else ''
            lines.append(f"**{dt}** (+{days_out}d) — {name}")
            lines.append(f"  📍 {addr}")
            lines.append(f"  💰 ${price:,.2f} total | ${due:,.2f} due")
            if tag_str:
                lines.append(f"  🏷️  {tag_str}")
            line_names = [li['Name'] for li in j.get('LineItems', [])]
            if line_names:
                lines.append(f"  🔧 {', '.join(line_names)}")
            lines.append("")
    else:
        lines += ["", "## Upcoming Jobs", "None scheduled in the next 30 days."]

    if recent:
        lines += ["", f"## Completed This Week", ""]
        for j in recent:
            name = f"{j.get('FirstName','')} {j.get('LastName','')}".strip() or j.get('Company', 'Unknown')
            price = j.get('JobTotalPrice', 0)
            lines.append(f"- {name} — ${price:,.2f} ({j.get('Status')})")

    # All jobs table
    lines += ["", "## All Power Washing Jobs", ""]
    lines.append("| Date | Client | Address | Value | Status |")
    lines.append("|------|--------|---------|-------|--------|")
    for j in sorted(jobs, key=lambda x: x.get('JobDateTime', ''), reverse=True):
        name = f"{j.get('FirstName','')} {j.get('LastName','')}".strip() or j.get('Company', 'N/A')
        addr = j.get('City', '') + ', ' + j.get('State', '')
        dt = j.get('JobDateTime', '')[:10]
        price = j.get('JobTotalPrice', 0)
        status = j.get('Status', '')
        lines.append(f"| {dt} | {name} | {addr} | ${price:,.2f} | {status} |")

    report = '\n'.join(lines)
    summary = f"{len(jobs)} Power Washing jobs | ${total_revenue:,.2f} total value | ${total_due:,.2f} outstanding"

    return {'report': report, 'jobs': jobs, 'summary': summary}


def save_report(report_text, mode='daily'):
    today = datetime.date.today().strftime('%Y-%m-%d')
    out_dir = os.path.join(os.path.dirname(__file__), '..', 'outputs', 'nina')
    os.makedirs(out_dir, exist_ok=True)
    filename = f"workiz_{mode}_{today}.md"
    filepath = os.path.join(out_dir, filename)
    with open(filepath, 'w') as f:
        f.write(report_text)
    print(f"Saved: {filepath}")
    return filepath


def log_activity(summary, mode='daily'):
    today = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    log_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'activity.log')
    with open(log_path, 'a') as f:
        f.write(f"[{today}] Nina | Workiz {mode} report - Power Washing jobs | {summary} | Done\n")


def post_to_slack(report_text, summary, mode='daily'):
    if not SLACK_WEBHOOK:
        print("No Slack webhook configured")
        return
    msg = f"*Nina Kowalski — Workiz Power Washing {mode.title()} Report*\n\n{report_text[:3500]}"
    payload = json.dumps({'text': msg}).encode()
    try:
        req = urllib.request.Request(SLACK_WEBHOOK, payload, {'Content-Type': 'application/json'})
        urllib.request.urlopen(req, timeout=10)
        print("Posted to Slack")
    except Exception as e:
        print(f"Slack post failed: {e}")


if __name__ == '__main__':
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else 'daily'

    print(f"Running Workiz {mode} report (Power Washing jobs only)...")
    result = generate_report(mode)

    filepath = save_report(result['report'], mode)
    log_activity(result['summary'], mode)
    post_to_slack(result['report'], result['summary'], mode)

    print(f"\n{result['summary']}")
    print(f"Report: {filepath}")
