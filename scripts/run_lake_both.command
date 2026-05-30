#!/bin/bash
# Double-click this file in Finder to run the full Lake County pull.
# Runs BOTH Danny (property managers + commercial segments) AND Carla (referral partners).
# June 15 (Week 25) — Mentor, Willoughby, Painesville, Eastlake, Wickliffe.
# No typing required. Takes 5-8 minutes total.

cd /Users/bradleyneal/forestcity
echo "============================================="
echo " Forest City — Lake County Full Pull"
echo " Danny (Property Managers) + Carla (Referral Partners)"
echo " $(date)"
echo "============================================="
echo ""
echo "Step 1 of 2: Danny — Property Managers + Commercial Segments..."
echo ""
python3 workers/lead_pipeline.py danny Lake
echo ""
echo "============================================="
echo "Step 2 of 2: Carla — Referral Partners..."
echo ""
python3 workers/lead_pipeline.py carla Lake
echo ""
echo "============================================="
echo "Both pulls complete."
echo "Check logs/activity.log for results."
echo "Lake County: Week 25 (June 15) — Marina corridor + Mentor suburbs."
echo ""
echo "Press any key to close."
read -n 1
