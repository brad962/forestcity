#!/usr/bin/env python3
"""
Report Card Generator — Forest City Power Washing AI Office
Generates a clean image report card for each worker and posts to Slack via file upload.
"""

import io
import json
import os
import urllib.request
import urllib.parse
from datetime import datetime
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# Font paths
FONT_BOLD   = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
FONT_REG    = '/System/Library/Fonts/Supplemental/Arial.ttf'
FONT_NARROW = '/System/Library/Fonts/Supplemental/Arial Narrow.ttf'

# Worker color themes
WORKER_THEMES = {
    'danny':   {'bg': (15, 23, 42),   'accent': (59, 130, 246),  'tag': '#OUTBOUND'},
    'carla':   {'bg': (15, 23, 42),   'accent': (168, 85, 247),  'tag': '#REFERRALS'},
    'nina':    {'bg': (15, 23, 42),   'accent': (20, 184, 166),  'tag': '#REVOPS'},
    'marcus':  {'bg': (15, 23, 42),   'accent': (245, 158, 11),  'tag': '#INTELLIGENCE'},
    'tommy':   {'bg': (15, 23, 42),   'accent': (239, 68, 68),   'tag': '#COPY'},
    'jasmine': {'bg': (15, 23, 42),   'accent': (236, 72, 153),  'tag': '#SOCIAL'},
    'rick':    {'bg': (15, 23, 42),   'accent': (249, 115, 22),  'tag': '#ADS'},
    'donna':   {'bg': (15, 23, 42),   'accent': (34, 197, 94),   'tag': '#STRATEGY'},
    'vera':    {'bg': (15, 23, 42),   'accent': (99, 102, 241),  'tag': '#INNOVATION'},
}

DEFAULT_THEME = {'bg': (15, 23, 42), 'accent': (100, 116, 139), 'tag': '#OFFICE'}

W, H = 900, 520


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()


def draw_rounded_rect(draw, xy, radius, fill):
    x0, y0, x1, y1 = xy
    draw.rectangle([x0 + radius, y0, x1 - radius, y1], fill=fill)
    draw.rectangle([x0, y0 + radius, x1, y1 - radius], fill=fill)
    draw.ellipse([x0, y0, x0 + radius * 2, y0 + radius * 2], fill=fill)
    draw.ellipse([x1 - radius * 2, y0, x1, y0 + radius * 2], fill=fill)
    draw.ellipse([x0, y1 - radius * 2, x0 + radius * 2, y1], fill=fill)
    draw.ellipse([x1 - radius * 2, y1 - radius * 2, x1, y1], fill=fill)


def generate_report_card(
    worker_name: str,
    title: str,
    metrics: list,       # list of (label, value) tuples — up to 4
    summary_lines: list, # list of strings for the summary section
    status: str = 'DONE',
    date: str = None,
) -> bytes:
    """
    Generate a report card image and return as PNG bytes.

    Args:
        worker_name: 'danny', 'nina', etc.
        title: Report title, e.g. 'Weekly Pipeline Report'
        metrics: [(label, value), ...] — up to 4 key metrics shown as big numbers
        summary_lines: list of bullet point strings shown in the lower section
        status: 'DONE', 'IN PROGRESS', 'ACTION NEEDED'
        date: date string, defaults to today
    """
    theme = WORKER_THEMES.get(worker_name.lower(), DEFAULT_THEME)
    bg    = theme['bg']
    acc   = theme['accent']
    date  = date or datetime.now().strftime('%B %d, %Y')

    img  = Image.new('RGB', (W, H), bg)
    draw = ImageDraw.Draw(img)

    # Subtle gradient-like top stripe
    for i in range(6):
        alpha = int(255 * (1 - i / 6))
        stripe_color = tuple(min(255, c + 30) for c in bg)
        draw.rectangle([0, i, W, i + 1], fill=stripe_color)

    # Accent bar left edge
    draw.rectangle([0, 0, 5, H], fill=acc)

    # Header area
    draw.rectangle([0, 0, W, 90], fill=tuple(min(255, c + 8) for c in bg))

    # Worker name pill
    pill_w = 160
    draw_rounded_rect(draw, [24, 18, 24 + pill_w, 52], 16, acc)
    wname = worker_name.upper()
    draw.text((24 + pill_w // 2, 35), wname,
              fill='white', font=font(FONT_BOLD, 16), anchor='mm')

    # Tag pill
    tag_text = theme['tag']
    tag_font = font(FONT_NARROW, 13)
    tag_w = draw.textlength(tag_text, font=tag_font) + 20
    draw_rounded_rect(draw, [200, 22, 200 + tag_w, 48], 13,
                      tuple(max(0, c - 10) for c in acc))
    draw.text((200 + tag_w // 2, 35), tag_text,
              fill='white', font=tag_font, anchor='mm')

    # Status pill (top right)
    status_colors = {
        'DONE':          (34, 197, 94),
        'IN PROGRESS':   (245, 158, 11),
        'ACTION NEEDED': (239, 68, 68),
    }
    sc = status_colors.get(status, (100, 116, 139))
    s_font = font(FONT_BOLD, 12)
    s_w = draw.textlength(status, font=s_font) + 24
    draw_rounded_rect(draw, [W - s_w - 24, 22, W - 24, 48], 13, sc)
    draw.text((W - 24 - s_w // 2, 35), status,
              fill='white', font=s_font, anchor='mm')

    # Date (right of status)
    draw.text((W - 24, 56), date,
              fill=(100, 116, 139), font=font(FONT_REG, 12), anchor='ra')

    # Title
    draw.text((24, 102), title,
              fill='white', font=font(FONT_BOLD, 26), anchor='la')

    # Divider
    draw.rectangle([24, 140, W - 24, 141],
                   fill=tuple(min(255, c + 20) for c in bg))

    # Metrics row (up to 4)
    if metrics:
        n = min(len(metrics), 4)
        cell_w = (W - 48) // n
        for i, (label, value) in enumerate(metrics[:4]):
            x = 24 + i * cell_w
            # Card background
            draw_rounded_rect(draw,
                [x + 6, 152, x + cell_w - 6, 248], 10,
                tuple(min(255, c + 12) for c in bg))
            # Accent top line
            draw.rectangle([x + 6, 152, x + cell_w - 6, 155], fill=acc)
            # Value (big number)
            val_str = str(value)
            v_font_size = 36 if len(val_str) <= 5 else 28
            draw.text((x + cell_w // 2, 188),
                      val_str, fill=acc,
                      font=font(FONT_BOLD, v_font_size), anchor='mm')
            # Label
            draw.text((x + cell_w // 2, 228),
                      label.upper(), fill=(148, 163, 184),
                      font=font(FONT_NARROW, 12), anchor='mm')

    # Summary section
    draw.rectangle([24, 262, W - 24, 263],
                   fill=tuple(min(255, c + 20) for c in bg))
    draw.text((24, 272), 'SUMMARY',
              fill=(100, 116, 139), font=font(FONT_BOLD, 11))

    y = 296
    bullet_font = font(FONT_REG, 15)
    for line in summary_lines[:6]:
        if y > H - 40:
            break
        # Bullet dot
        draw.ellipse([24, y + 5, 30, y + 11], fill=acc)
        # Clip line if too long
        max_w = W - 70
        while draw.textlength(line, font=bullet_font) > max_w and len(line) > 10:
            line = line[:-4] + '...'
        draw.text((38, y), line, fill=(226, 232, 240), font=bullet_font)
        y += 28

    # Footer bar
    draw.rectangle([0, H - 36, W, H], fill=tuple(max(0, c - 5) for c in bg))
    draw.text((24, H - 20),
              'Forest City Power Washing — AI Office',
              fill=(71, 85, 105), font=font(FONT_NARROW, 12), anchor='lm')
    draw.text((W - 24, H - 20),
              f'forestcitypowerwashing.com',
              fill=(71, 85, 105), font=font(FONT_NARROW, 12), anchor='rm')

    buf = io.BytesIO()
    img.save(buf, format='PNG', optimize=True)
    return buf.getvalue()


def push_image_to_github(
    png_bytes: bytes,
    repo_path: str,
    github_pat: str,
) -> str:
    """Push PNG to GitHub and return the raw URL for Slack preview."""
    import base64, time
    repo    = 'brad962/forestcity'
    api_url = f'https://api.github.com/repos/{repo}/contents/{repo_path}'

    # Check if file exists (need SHA to update)
    sha = None
    try:
        req = urllib.request.Request(api_url, headers={'Authorization': f'token {github_pat}', 'User-Agent': 'forestcity'})
        with urllib.request.urlopen(req) as resp:
            sha = json.loads(resp.read()).get('sha')
    except Exception:
        pass

    payload = {
        'message': f'Report card: {repo_path}',
        'content': base64.b64encode(png_bytes).decode(),
        'branch':  'main',
    }
    if sha:
        payload['sha'] = sha

    req = urllib.request.Request(
        api_url,
        data=json.dumps(payload).encode(),
        headers={
            'Authorization': f'token {github_pat}',
            'Content-Type':  'application/json',
            'User-Agent':    'forestcity',
        },
        method='PUT'
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        json.loads(resp.read())

    cache_bust = int(time.time())
    return f'https://raw.githubusercontent.com/{repo}/main/{repo_path}?v={cache_bust}'


def post_image_to_slack(
    png_bytes: bytes,
    filename: str,
    title: str,
    worker_name: str,
    slack_webhook: str,
    github_pat: str,
) -> bool:
    """Push image to GitHub then post URL to Slack so it previews inline."""
    try:
        repo_path = f'outputs/{worker_name}/reports/{filename}'
        image_url = push_image_to_github(png_bytes, repo_path, github_pat)

        payload = json.dumps({
            'text':        f'*{title}*',
            'attachments': [{'image_url': image_url, 'fallback': title}],
        }).encode()
        req = urllib.request.Request(
            slack_webhook, payload,
            {'Content-Type': 'application/json'}
        )
        urllib.request.urlopen(req, timeout=10)
        return True
    except Exception as e:
        print(f'Image post failed: {e}')
        return False


def send_report_card(
    worker_name: str,
    title: str,
    metrics: list,
    summary_lines: list,
    status: str = 'DONE',
    date: str = None,
) -> bool:
    """
    Generate a report card image, push to GitHub, and post to Slack.
    Loads all credentials from .env automatically.
    """
    # Load env
    env_file = Path(__file__).parent.parent / '.env'
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                os.environ.setdefault(k.strip(), v.strip())

    webhook    = os.environ.get('SLACK_WEBHOOK_OFFICE', '')
    github_pat = os.environ.get('GITHUB_PAT', '')

    if not webhook or not github_pat:
        print('Missing SLACK_WEBHOOK_OFFICE or GITHUB_PAT')
        return False

    # Ensure output dir exists locally too
    out_dir = Path(__file__).parent.parent / 'outputs' / worker_name / 'reports'
    out_dir.mkdir(parents=True, exist_ok=True)

    date_str = date or datetime.now().strftime('%Y-%m-%d')
    filename = f'{worker_name}_report_{date_str}.png'

    png = generate_report_card(worker_name, title, metrics, summary_lines, status, date)

    # Save locally
    (out_dir / filename).write_bytes(png)

    ok = post_image_to_slack(png, filename, title, worker_name, webhook, github_pat)

    if ok:
        print(f'Report card posted to Slack for {worker_name}')
    else:
        print(f'Failed to post report card for {worker_name}')
    return ok


# ── Quick test ───────────────────────────────────────────────────────────────
if __name__ == '__main__':
    import sys
    worker = sys.argv[1] if len(sys.argv) > 1 else 'nina'

    samples = {
        'nina': (
            'Weekly Pipeline Report',
            [('Enrolled', 45), ('Opens', 19), ('Hot Leads', 13), ('Replies', 0)],
            [
                '42% overall open rate across all sequences',
                'Property Managers leading at 59% open rate',
                '13 contacts opened 2+ times — prime for LinkedIn',
                'Realtors at 40%, Contractors at 28%',
                '0 replies yet — sequence rewrite proposed',
            ],
            'ACTION NEEDED',
        ),
        'danny': (
            'Weekly Lead Pull',
            [('Pulled', 25), ('Enrolled', 24), ('Repaired', 0), ('Failed', 1)],
            [
                '25 new property managers from Cuyahoga County',
                'Enrolled in Property Manager sequence',
                'Enrollment verification passed — all confirmed',
                'Top targets: facility managers + community managers',
            ],
            'DONE',
        ),
        'vera': (
            'Hourly Office Scan',
            [('Upgrades', 8), ('Proposals', 3), ('Open Issues', 6), ('Fixed', 2)],
            [
                'Fixed Jasmine infinite retry loop',
                'Mixmax token moved from hardcode to .env',
                'Carla expanded to all 7 NE Ohio counties',
                'Workiz case-insensitive job matching deployed',
                '2 hot contractors waiting for text from Bradley',
            ],
            'ACTION NEEDED',
        ),
    }

    w, (title, metrics, summary, status) = worker, samples.get(worker, samples['nina'])

    # Save locally first to preview
    png = generate_report_card(w, title, metrics, summary, status)
    out = Path(f'/tmp/{w}_report_preview.png')
    out.write_bytes(png)
    print(f'Preview saved: {out}')

    # Post to Slack
    result = send_report_card(w, title, metrics, summary, status)
    print('Posted:', result)
