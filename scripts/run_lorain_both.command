#!/bin/bash
# Double-click this file in Finder to run the full Lorain County pull.
# Runs BOTH Danny (property managers + commercial segments) AND Carla (referral partners).
# June 22 (Week 26) — Elyria, Avon, North Ridgeville, Vermilion, Amherst.
# No typing required. Takes 5-8 minutes total.

cd /Users/bradleyneal/forestcity
echo "============================================="
echo " Forest City — Lorain County Full Pull"
echo " Danny (Property Managers) + Carla (Referral Partners)"
echo " $(date)"
echo "============================================="
echo ""
echo "Step 1 of 2: Danny — Property Managers + Commercial Segments..."
echo ""
python3 workers/lead_pipeline.py danny Lorain
echo ""
echo "============================================="
echo "Step 2 of 2: Carla — Referral Partners..."
echo ""
python3 workers/lead_pipeline.py carla Lorain
echo ""
echo "============================================="
echo "Both pulls complete."
echo "Check logs/activity.log for results."
echo "Lorain County: Week 26 (June 22) — Avon corridor + harbor marinas."
echo ""
echo "Press any key to close."
read -n 1
