#!/bin/bash
# Runs the full Jasmine pipeline: watch for new photos → build flyer → post to Slack
# Called by launchd every 5 minutes

cd /Users/bradleyneal/forestcity

# Add site-packages to PYTHONPATH for third-party libraries
export PYTHONPATH="/Users/bradleyneal/Library/Python/3.9/lib/python/site-packages:$PYTHONPATH"

# Load .env
set -o allexport
source /Users/bradleyneal/forestcity/.env
set +o allexport

echo "[$(date)] Starting photo watcher..." >> /Users/bradleyneal/forestcity/logs/cron.log

# Step 1: Check Slack #fc-requests for new photos
/usr/bin/python3 workers/slack_photo_watcher.py >> /Users/bradleyneal/forestcity/logs/cron.log 2>&1

# Step 2: Process any new pairs with Jasmine
/usr/bin/python3 workers/jasmine_flyer.py >> /Users/bradleyneal/forestcity/logs/cron.log 2>&1

echo "[$(date)] Pipeline complete." >> /Users/bradleyneal/forestcity/logs/cron.log
