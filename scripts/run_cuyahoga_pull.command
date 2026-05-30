#!/bin/bash
# Double-click this file in Finder to run the Cuyahoga County lead pull.
# June 8 (Week 24) — LARGEST market: Cleveland, Parma, Lakewood, Strongsville, Beachwood.
# No typing required.

cd /Users/bradleyneal/forestcity
echo "========================================"
echo " Forest City — Cuyahoga County Lead Pull"
echo " $(date)"
echo "========================================"
echo ""
echo "Pulling Cuyahoga County leads from Apollo..."
echo "NOTE: 51+ commercial segments active (hospitals, museums, DSOs, government,"
echo "      breweries, sports venues, dispensaries, dialysis centers + more)."
echo "This run uses title + org keyword batching and will take 8-15 minutes."
echo "Let it run unattended — do not close this window."
echo ""
python3 workers/lead_pipeline.py danny Cuyahoga
echo ""
echo "========================================"
echo "Done. Check logs/activity.log for results."
echo "Press any key to close."
read -n 1
