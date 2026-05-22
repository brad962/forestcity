# GitHub PAT — Add Workflow Scope (3 Minutes)
### Vera Cole | Chief Innovation Officer
*Created: 2026-05-22 | Blocks: Cloud Slack delivery via GitHub Actions*

---

## Why This Matters

Every time Vera pushes code from the cloud, the updates sit in `pending_slack_messages.md` but can't be posted to Slack automatically — because the GitHub Action that would post them requires a workflow file in `.github/workflows/`, and GitHub blocks pushing that file without `workflow` scope in the Personal Access Token (PAT).

**Once you add this scope:** Every Vera push will automatically post updates to Slack within 60 seconds. No more checking the repo manually.

The PAT currently in use starts with `ghp_lrUh...` — you know which one it is (check your password manager or .env file).

---

## 3-Step Fix

### Step 1: Go to your PAT settings
Direct URL: [github.com/settings/tokens](https://github.com/settings/tokens)

Or: GitHub.com → Profile photo (top right) → Settings → Developer settings → Personal access tokens → Tokens (classic)

### Step 2: Edit the existing token
Find the token used for forestcity (the one starting with `ghp_lrUh...`).
Click **Edit** next to it.

Under **Select scopes**, check the box next to:
```
✅ workflow — Update GitHub Action workflows
```

It's in the "repo" section, just below the main repo checkboxes.

Click **Update token** at the bottom.

### Step 3: Copy the new token value
GitHub will show the new token value. **Copy it now** — you won't see it again.

Update it in any place you've stored the token (password manager, .env file if it's there).

---

## After Adding the Scope

Run the deploy script from your Mac terminal:
```bash
cd /Users/bradleyneal/forestcity
bash scripts/deploy_github_action.sh
```

This pushes `.github/workflows/vera-slack-relay.yaml` to the repo and activates the GitHub Action.

Then add one GitHub repo secret:
1. Go to: github.com/brad962/forestcity → Settings → Secrets and variables → Actions
2. Click **New repository secret**
3. Name: `SLACK_WEBHOOK_OFFICE`
4. Value: your Slack webhook URL (from Slack API settings or your `.env` file)
5. Click **Add secret**

That's it. Next Vera push → Slack message within 60 seconds.

---

## Current Workaround Status

Until this is done, vera_relay.py on your local crontab handles Slack delivery:
```
*/5 * * * * cd /Users/bradleyneal/forestcity && python3 workers/vera_relay.py >> logs/cron.log 2>&1
```
This works as long as your Mac is on and the crontab is installed (`scripts/crontab_setup.txt`).
