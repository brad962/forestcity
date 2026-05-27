#!/bin/bash
# Double-click this file in Finder to run the Summit County lead pull.
# It opens Terminal, changes to the project directory, and runs the pull.
# No typing required.

cd /Users/bradleyneal/forestcity
echo "========================================"
echo " Forest City — Summit County Lead Pull"
echo " $(date)"
echo "========================================"
echo ""
echo "Pulling Summit County leads from Apollo..."
echo "NOTE: 20+ new commercial segments added. Run takes 5-10 minutes."
echo "Let it run unattended — DO NOT close this window."
echo ""
python3 workers/lead_pipeline.py danny Summit
echo ""
echo "========================================"
echo "Done. Check logs/activity.log for results."
echo "Press any key to close."
read -n 1
