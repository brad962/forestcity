#!/bin/bash
# Deploy the Vera Slack Relay GitHub Action
# Run this ONCE from your Mac: bash /Users/bradleyneal/forestcity/scripts/deploy_github_action.sh
#
# Prerequisites (one-time, ~3 min total):
#   1. Add 'workflow' scope to your PAT:
#      github.com → Settings → Developer settings → Personal access tokens
#      → Edit token ghp_lrUhBq7... → check 'workflow' box → Save
#   2. Add SLACK_WEBHOOK_OFFICE as a repo secret:
#      github.com/brad962/forestcity → Settings → Secrets and variables → Actions
#      → New repository secret → Name: SLACK_WEBHOOK_OFFICE
#      → Value: (paste your Slack webhook URL from .env)
#
# After those two steps, run this script. Every Vera push will then auto-post to Slack.

set -e

REPO_DIR="/Users/bradleyneal/forestcity"

# ── Pre-flight: verify PAT has 'workflow' scope ─────────────────────────────
echo "→ Pre-flight check: GitHub PAT scope"
PAT=$(git -C "$REPO_DIR" remote get-url origin 2>/dev/null | sed 's|https://||;s|@.*||')
if [ -n "$PAT" ]; then
    SCOPES=$(curl -sI -H "Authorization: token $PAT" https://api.github.com/user 2>/dev/null | grep -i '^x-oauth-scopes:' || true)
    if echo "$SCOPES" | grep -q "workflow"; then
        echo "  ✅ PAT has 'workflow' scope — good to go."
    else
        echo ""
        echo "❌  PAT is missing 'workflow' scope."
        echo "    Push will be rejected by GitHub. Fix first (2 minutes):"
        echo ""
        echo "    1. Open: https://github.com/settings/tokens"
        echo "    2. Find your token (starts with ghp_lrUhBq7...)"
        echo "    3. Click Edit → check the ☑ 'workflow' box → Update token"
        echo "    4. Re-run this script."
        echo ""
        exit 1
    fi
else
    echo "  ⚠️  Could not extract PAT from remote URL — continuing without scope check."
    echo "     If the push fails with 'refusing to allow', add 'workflow' scope at github.com/settings/tokens"
fi
echo ""
# ────────────────────────────────────────────────────────────────────────────
WORKFLOW_SRC="$REPO_DIR/outputs/vera/github_action_vera_slack_relay.yaml"
WORKFLOW_DST="$REPO_DIR/.github/workflows/vera-slack-relay.yaml"

echo "→ Creating .github/workflows/ directory..."
mkdir -p "$REPO_DIR/.github/workflows"

echo "→ Copying workflow file..."
cp "$WORKFLOW_SRC" "$WORKFLOW_DST"

echo "→ Staging workflow file..."
cd "$REPO_DIR"
git add .github/workflows/vera-slack-relay.yaml

echo "→ Committing..."
git commit -m "Add Vera Slack relay GitHub Action — auto-posts pending_slack_messages.md on each Vera push"

echo "→ Pushing to GitHub..."
git push origin main

echo ""
echo "✅ Done! GitHub Actions tab should show the workflow now."
echo "   First Vera push after this will trigger a test run."
echo "   Check: https://github.com/brad962/forestcity/actions"
