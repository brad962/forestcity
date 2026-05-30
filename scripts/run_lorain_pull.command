#!/bin/bash
# Double-click this file in Finder to run the Lorain County lead pull.
# June 22 (Week 26) — Elyria, Avon, North Ridgeville, Vermilion, Amherst.
# Avon = fastest-growing NE Ohio suburb. Lorain Harbor marina corridor.
# No typing required.

cd /Users/bradleyneal/forestcity
echo "========================================"
echo " Forest City — Lorain County Lead Pull"
echo " $(date)"
echo "========================================"
echo ""
echo "Pulling Lorain County leads from Apollo..."
echo "NOTE: Avon/Avon Lake = fastest-growing NE Ohio suburb; strong HOA density."
echo "      Lorain Harbor marina corridor + Vermilion Lake Erie shoreline."
echo "      Also: Rt 83 industrial corridor (self-storage, auto body, distribution)."
echo "This run will take 5-10 minutes — let it run unattended."
echo ""
python3 workers/lead_pipeline.py danny Lorain
echo ""
echo "========================================"
echo "Done. Check logs/activity.log for results."
echo "Press any key to close."
read -n 1
