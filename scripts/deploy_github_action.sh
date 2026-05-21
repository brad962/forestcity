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
