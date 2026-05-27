#!/bin/bash
# Double-click this file in Finder to run the Medina County lead pull.
# It opens Terminal, changes to the project directory, and runs the pull.
# No typing required.

cd /Users/bradleyneal/forestcity
echo "========================================"
echo " Forest City — Medina County Lead Pull"
echo " $(date)"
echo "========================================"
echo ""
echo "Pulling Medina County leads from Apollo..."
echo "NOTE: 20+ new commercial segments added since last pull."
echo "This run will take 5-10 minutes — let it run unattended."
echo ""
python3 workers/lead_pipeline.py danny Medina
echo ""
echo "========================================"
echo "Done. Check logs/activity.log for results."
echo "Press any key to close."
read -n 1
