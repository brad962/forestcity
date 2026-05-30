#!/bin/bash
# Double-click this file in Finder to run the Lake County lead pull.
# June 15 (Week 25) — Mentor, Willoughby, Painesville, Eastlake, Madison Township.
# MARINA CORRIDOR: Mentor Harbor, Sheffield Lake, Euclid shoreline.
# No typing required.

cd /Users/bradleyneal/forestcity
echo "========================================"
echo " Forest City — Lake County Lead Pull"
echo " $(date)"
echo "========================================"
echo ""
echo "Pulling Lake County leads from Apollo..."
echo "NOTE: Marina segment — Mentor Harbor, Sheffield Lake, Euclid shoreline."
echo "      Also: Mentor Headlands waterfront properties + Lake Erie industrial corridor."
echo "This run will take 5-10 minutes — let it run unattended."
echo ""
python3 workers/lead_pipeline.py danny Lake
echo ""
echo "========================================"
echo "Done. Check logs/activity.log for results."
echo "Press any key to close."
read -n 1
