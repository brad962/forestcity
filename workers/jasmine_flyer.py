#!/usr/bin/env python3
"""
Jasmine's before/after flyer builder.
Takes before + after photos, stitches them side-by-side with the logo
floating in the center (rounded white pill background), then pushes to
#fc-ai-office via GitHub raw URL + Slack chat.postMessage.
"""

import os
import sys
import json
import base64
import time
import requests
from pathlib import Path
from datetime import datetime

try:
    from PIL import Image, ImageDraw
    _PIL_AVAILABLE = True
except ImportError:
    _PIL_AVAILABLE = False

BASE_DIR   = Path(__file__).parent.parent
ASSETS_DIR = BASE_DIR / "assets"
OUTPUTS_DIR = BASE_DIR / "outputs" / "jasmine"
LOGS_DIR   = BASE_DIR / "logs"
PHOTO_PAIRS_FILE = LOGS_DIR / "photo_pairs.json"
ACTIVITY_LOG     = LOGS_DIR / "activity.log"


def _load_env():
    env_file = BASE_DIR / '.env'
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                os.environ.setdefault(k.strip(), v.strip())


_load_env()

SLACK_TOKEN   = os.environ.get("SLACK_TOKEN", "")
SLACK_CHANNEL = "C0B37D5UJLB"   # fc-ai-office
GITHUB_PAT    = os.environ.get("GITHUB_PAT", "")
GITHUB_REPO   = "brad962/forestcity"

PANEL_WIDTH   = 900
PANEL_HEIGHT  = 900
LOGO_MAX_W    = 420
LOGO_MAX_H    = 180
LOGO_PADDING  = 20
CORNER_RADIUS = 16


def log(msg):
    ts   = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] Jasmine: {msg}"
    print(line)
    LOGS_DIR.mkdir(exist_ok=True)
    with open(ACTIVITY_LOG, "a") as f:
        f.write(line + "\n")


def fit_image(img: "Image.Image", width: int, height: int) -> "Image.Image":
    """Cover-crop image to exactly width x height."""
    r  = img.width / img.height
    tr = width / height
    if r > tr:
        nw, nh = int(r * height), height
    else:
        nw, nh = width, int(width / r)
    img  = img.resize((nw, nh), Image.LANCZOS)
    left = (nw - width)  // 2
    top  = (nh - height) // 2
    return img.crop((left, top, left + width, top + height))


def build_flyer(before_path: str, after_path: str, output_path: str) -> str:
    """
    Build the before/after composite:
      - Before photo on the left half
      - After photo on the right half
      - Logo centered with a rounded white pill background
    """
    if not _PIL_AVAILABLE:
        raise RuntimeError(
            "Pillow (PIL) is not installed. Run `pip install Pillow` to enable flyer generation."
        )
    logo_path = ASSETS_DIR / "logo.png"
    if not logo_path.exists():
        raise FileNotFoundError(f"Logo not found at {logo_path}")

    before = fit_image(Image.open(before_path).convert("RGB"), PANEL_WIDTH, PANEL_HEIGHT)
    after  = fit_image(Image.open(after_path).convert("RGB"),  PANEL_WIDTH, PANEL_HEIGHT)
    logo   = Image.open(logo_path).convert("RGBA")
    logo.thumbnail((LOGO_MAX_W, LOGO_MAX_H), Image.LANCZOS)

    # Canvas: two photos side by side, no gap
    canvas = Image.new("RGB", (PANEL_WIDTH * 2, PANEL_HEIGHT))
    canvas.paste(before, (0, 0))
    canvas.paste(after,  (PANEL_WIDTH, 0))

    lw, lh = logo.size
    logo_x = (PANEL_WIDTH * 2 - lw) // 2
    logo_y = (PANEL_HEIGHT - lh)    // 2

    # Rounded white pill behind logo (slightly transparent)
    pill_w = lw + LOGO_PADDING * 2
    pill_h = lh + LOGO_PADDING * 2
    pill   = Image.new("RGBA", (pill_w, pill_h), (0, 0, 0, 0))
    draw   = ImageDraw.Draw(pill)
    draw.rounded_rectangle([0, 0, pill_w, pill_h], radius=CORNER_RADIUS, fill=(255, 255, 255, 230))
    canvas.paste(
        Image.new("RGB", pill.size, (255, 255, 255)),
        (logo_x - LOGO_PADDING, logo_y - LOGO_PADDING),
        mask=pill.split()[3],
    )

    # Logo on top — transparent background already handled
    canvas.paste(logo, (logo_x, logo_y), mask=logo.split()[3])

    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
    canvas.save(output_path, "JPEG", quality=92)
    return output_path


def push_to_github(file_path: str, github_path: str, commit_msg: str) -> str:
    """Push file to GitHub and return the raw URL."""
    with open(file_path, "rb") as f:
        content = base64.b64encode(f.read()).decode()

    check = requests.get(
        f"https://api.github.com/repos/{GITHUB_REPO}/contents/{github_path}",
        headers={"Authorization": f"token {GITHUB_PAT}"},
    )
    sha     = check.json().get("sha") if check.status_code == 200 else None
    payload = {"message": commit_msg, "content": content}
    if sha:
        payload["sha"] = sha

    r = requests.put(
        f"https://api.github.com/repos/{GITHUB_REPO}/contents/{github_path}",
        headers={"Authorization": f"token {GITHUB_PAT}", "Content-Type": "application/json"},
        json=payload,
    )
    r.raise_for_status()
    raw_url = f"https://raw.githubusercontent.com/{GITHUB_REPO}/main/{github_path}?v={int(time.time())}"
    return raw_url


def write_facebook_post(description: str, date: str) -> str:
    """
    Generate a Facebook post from a job description using Jasmine's voice.
    Format: scroll-stopping hook → job details → soft CTA → hashtags
    Varies hook and CTA by month for seasonal relevance.
    """
    try:
        dt = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        dt = datetime.now()
    month = dt.strftime("%B")
    mo    = dt.month
    day   = dt.day
    desc  = description.strip()

    # When past mid-month, say "booking into NEXT month" — "booking into May" on May 20 is wrong
    if day >= 15:
        next_mo = mo % 12 + 1
        next_yr = dt.year + (1 if next_mo == 1 else 0)
        booking_month = dt.replace(year=next_yr, month=next_mo, day=1).strftime("%B")
    else:
        booking_month = month

    if mo in (3, 4, 5):
        hook = "The algae doesn't care that it's spring. Your neighbors do."
        cta  = f"We're booking into {booking_month} now — DM us or comment QUOTE to get on the schedule before the summer rush."
    elif mo in (6, 7, 8):
        hook = "Before the cookout. Before the guests. Before the photos."
        cta  = f"Summer slots are filling fast — DM us or comment QUOTE and we'll get you on the {booking_month} schedule."
    elif mo in (9, 10):
        hook = "One job before winter and your house is protected all season."
        cta  = "Fall slots go fast — DM us or comment QUOTE to lock in your date."
    else:
        hook = "Clean house. Less stress. One afternoon."
        cta  = "DM us or comment QUOTE to get on the schedule."

    post = f"""{hook}

{desc}

One visit and it looks like a completely different property. We serve the greater Cleveland area and we're booking now.

📞 {cta}

#ClevelandOhio #NortheastOhio #PowerWashing #CurbAppeal #ForestCityPowerWashing"""

    return post.strip()


def post_to_slack(image_url: str, caption: str, facebook_post: str = "") -> bool:
    """Post image block + optional Facebook copy to Slack channel."""
    blocks = [
        {"type": "section", "text": {"type": "mrkdwn", "text": f"*{caption}*"}},
        {"type": "image",   "image_url": image_url, "alt_text": "Before and after power washing"},
    ]

    if facebook_post:
        blocks.append({"type": "divider"})
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*📱 Facebook Post — ready to copy/paste:*\n\n```{facebook_post}```"
            }
        })

    r = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers={"Authorization": f"Bearer {SLACK_TOKEN}", "Content-Type": "application/json"},
        json={
            "channel": SLACK_CHANNEL,
            "text": caption,
            "blocks": blocks,
        },
    )
    result = r.json()
    if not result.get("ok"):
        raise RuntimeError(f"Slack post failed: {result.get('error')}")
    return True


def process_pending_pairs():
    """Find unprocessed photo pairs, build flyers, push to GitHub, post to Slack."""
    if not PHOTO_PAIRS_FILE.exists():
        log("No photo_pairs.json found — nothing to process.")
        return

    try:
        data = json.loads(PHOTO_PAIRS_FILE.read_text())
    except (json.JSONDecodeError, Exception) as e:
        log(f"ERROR reading photo_pairs.json: {e} — skipping.")
        return
    pairs   = data.get("pairs", [])
    updated = False

    for pair in pairs:
        if pair.get("processed"):
            continue

        before_path = BASE_DIR / pair["before"]
        after_path  = BASE_DIR / pair["after"]
        pair_id     = pair["id"]
        date        = pair.get("date", datetime.now().strftime("%Y-%m-%d"))
        description = pair.get("description", "")

        if not before_path.exists() or not after_path.exists():
            log(f"Skipping {pair_id} — photo files missing.")
            continue

        log(f"Processing pair {pair_id}...")

        # Use pair_id suffix to prevent filename collision when multiple pairs share the same date
        pair_suffix     = pair_id[-8:] if len(pair_id) >= 8 else pair_id
        output_filename = f"before_after_{date}_{pair_suffix}.jpg"
        output_file     = OUTPUTS_DIR / output_filename
        github_path     = f"outputs/jasmine/{output_filename}"

        # Always mark as processed to prevent infinite retry loops on persistent errors.
        # Use pair["success"] to distinguish clean runs from failed ones.
        pair["processed"] = True
        pair["output"]    = str(output_file.relative_to(BASE_DIR))
        updated = True

        try:
            build_flyer(str(before_path), str(after_path), str(output_file))
            log(f"Flyer built → {output_file}")

            raw_url = push_to_github(str(output_file), github_path, f"Before/after flyer {date}")
            log(f"Pushed to GitHub → {raw_url}")

            facebook_post = ""
            if description:
                facebook_post = write_facebook_post(description, date)
                log("Facebook post written ✓")

            post_to_slack(raw_url, f"Before & After — Forest City Power Washing | {date}", facebook_post)
            log("Posted to #fc-ai-office ✓")
            pair["success"] = True

        except Exception as e:
            pair["success"] = False
            pair["error"]   = str(e)
            log(f"ERROR processing {pair_id}: {e}")

    if updated:
        PHOTO_PAIRS_FILE.write_text(json.dumps(data, indent=2))
        log("photo_pairs.json updated.")


if __name__ == "__main__":
    process_pending_pairs()
