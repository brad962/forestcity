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
echo "Pulling Summit County property managers from Apollo..."
echo "This takes about 2-3 minutes."
echo ""
python3 workers/lead_pipeline.py danny Summit
echo ""
echo "========================================"
echo "Done. Check logs/activity.log for results."
echo "Press any key to close."
read -n 1
