#!/bin/bash
# Danny Cron Health Check — run this on your Mac to verify the lead pipeline is running
# Usage: bash scripts/danny_cron_check.sh

LOGFILE="$HOME/forestcity/logs/cron.log"
ACTLOG="$HOME/forestcity/logs/activity.log"

echo "========================================"
echo "Danny Cron Health Check — $(date '+%Y-%m-%d %H:%M')"
echo "========================================"

echo ""
echo "=== 1. Active crontab entries ==="
crontab -l 2>/dev/null | grep -i "lead_pipeline\|vera_relay\|nina_report\|workiz" || echo "  ⚠️  No matching cron jobs found — run: crontab -e and paste from scripts/crontab_setup.txt"

echo ""
echo "=== 2. launchd plist (more reliable than cron on macOS) ==="
if ls ~/Library/LaunchAgents/com.forestcity.danny.plist &>/dev/null; then
    echo "  ✅ com.forestcity.danny.plist installed"
    launchctl list | grep forestcity || echo "  ⚠️  Not loaded — run: launchctl load ~/Library/LaunchAgents/com.forestcity.danny.plist"
else
    echo "  ⚠️  LaunchAgent not installed. Install with:"
    echo "     cp scripts/danny_launchd_plist.xml ~/Library/LaunchAgents/com.forestcity.danny.plist"
    echo "     launchctl load ~/Library/LaunchAgents/com.forestcity.danny.plist"
fi

echo ""
echo "=== 3. Last Danny lead pull (activity.log) ==="
if [ -f "$ACTLOG" ]; then
    LAST=$(grep "Danny.*Apollo pull" "$ACTLOG" | tail -1)
    if [ -n "$LAST" ]; then
        echo "  $LAST"
        # Extract date and compute days
        PULL_DATE=$(echo "$LAST" | grep -o '[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}' | head -1)
        TODAY=$(date '+%Y-%m-%d')
        if command -v python3 &>/dev/null; then
            DAYS=$(python3 -c "from datetime import date; d=date.fromisoformat('$PULL_DATE'); print((date.today()-d).days)")
            echo "  → $DAYS days ago"
            if [ "$DAYS" -ge 7 ]; then
                echo "  🔴 OVERDUE — run: cd ~/forestcity && python3 workers/lead_pipeline.py danny"
            else
                echo "  ✅ Within 7 days — on schedule"
            fi
        fi
    else
        echo "  ⚠️  No Danny pull found in activity.log"
    fi
else
    echo "  ⚠️  activity.log not found at $ACTLOG"
fi

echo ""
echo "=== 4. Last 10 cron.log entries ==="
if [ -f "$LOGFILE" ]; then
    tail -10 "$LOGFILE"
else
    echo "  ⚠️  cron.log not found — cron has not run yet (or wrong path)"
fi

echo ""
echo "=== 5. Manual run command ==="
echo "  cd ~/forestcity && python3 workers/lead_pipeline.py danny"
echo ""
echo "========================================"
