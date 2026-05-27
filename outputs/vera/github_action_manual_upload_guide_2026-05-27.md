# GitHub Action Manual Upload Guide
### Vera Cole | 2026-05-27 | Run 104
*Use this if the automatic push keeps failing (PAT may lack `workflow` scope)*

---

## Why This Matters

Every time Vera pushes changes to GitHub, the GitHub Action automatically reads `pending_slack_messages.md` and posts all queued Slack messages. Without this Action, Slack delivery depends on `vera_relay.py` running locally on your Mac — which breaks when your Mac is off or sleeping.

**This is a 3-minute one-time fix via your browser. No PAT upgrade needed.**

---

## The Fix: Create the Workflow File via GitHub Web UI

**Step 1: Open your repo on GitHub**
Go to: https://github.com/brad962/forestcity

**Step 2: Navigate to the Actions tab**
- Click the **Actions** tab (top nav bar of the repo page)
- If you see "Get started with GitHub Actions" click **"set up a workflow yourself"**
- If you already have other Actions, click **"New workflow"** → **"set up a workflow yourself"**

**Step 3: Name the file**
At the top of the editor where it says `main.yml`, change it to:
```
vera_slack_relay.yml
```

**Step 4: Paste the YAML content**
Select all text in the editor and replace with the exact content from:
`outputs/vera/github_action_vera_slack_relay.yaml`

Or paste this directly:

```yaml
name: Vera Slack Relay

on:
  push:
    branches: [main]
    paths:
      - 'outputs/vera/pending_slack_messages.md'

jobs:
  post-to-slack:
    runs-on: ubuntu-latest
    if: contains(github.event.head_commit.author.name, 'Vera')

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Read and post Slack messages
        env:
          SLACK_WEBHOOK: ${{ secrets.SLACK_WEBHOOK_OFFICE }}
        run: |
          python3 - <<'PYEOF'
          import os, json, urllib.request, sys

          webhook = os.environ.get('SLACK_WEBHOOK', '')
          if not webhook:
              print('ERROR: SLACK_WEBHOOK_OFFICE secret not configured.')
              sys.exit(1)

          pending_file = 'outputs/vera/pending_slack_messages.md'
          try:
              content = open(pending_file).read().strip()
          except FileNotFoundError:
              print('No pending_slack_messages.md found.')
              sys.exit(0)

          if not content or len(content) < 10:
              sys.exit(0)

          messages = [m.strip() for m in content.split('---') if m.strip() and len(m.strip()) > 10]
          posted = 0
          for msg in messages:
              try:
                  payload = json.dumps({'text': msg[:3000]}).encode()
                  req = urllib.request.Request(webhook, payload, {'Content-Type': 'application/json'})
                  urllib.request.urlopen(req, timeout=10)
                  posted += 1
              except Exception as e:
                  print(f'Failed: {e}')
          print(f'{posted}/{len(messages)} messages posted.')
          PYEOF

      - name: Clear pending messages
        run: echo "" > outputs/vera/pending_slack_messages.md

      - name: Commit cleared file
        run: |
          git config user.email "vera@forestcitypowerwashing.com"
          git config user.name "Vera Cole"
          git add outputs/vera/pending_slack_messages.md
          git diff --staged --quiet || git commit -m "Vera Relay: cleared pending Slack messages after GitHub Action post"
          git push origin main || echo "Nothing to push"
```

**Step 5: Add the Slack secret (if not already done)**
- In the repo, go to: **Settings** → **Secrets and variables** → **Actions** → **New repository secret**
- Name: `SLACK_WEBHOOK_OFFICE`
- Value: your Slack webhook URL (same as the one in your local `.env` file)
- Click "Add secret"

**Step 6: Commit the workflow file**
- Click **"Commit changes..."** (green button, top right)
- Commit directly to main
- Click **"Commit changes"**

**Done. ✅**

---

## How to Verify It's Working

1. Go to the **Actions** tab in your repo
2. You should see "Vera Slack Relay" in the workflow list
3. On the next Vera push that modifies `pending_slack_messages.md`, the Action fires automatically
4. You'll see a green checkmark next to the run in the Actions tab

---

## Notes

- Once deployed, `vera_relay.py` (local cron every 5 min) is still your fallback. Both can coexist.
- The Action only fires when `pending_slack_messages.md` changes AND the commit author contains "Vera"
- If the Action fails, check: (1) SLACK_WEBHOOK_OFFICE secret is set, (2) the webhook URL is still valid
