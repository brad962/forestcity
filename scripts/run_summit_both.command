#!/bin/bash
# Double-click this file in Finder to run the full Summit County pull.
# Runs BOTH Danny (property managers) AND Carla (referral partners) for Summit County.
# No typing required. Takes 5-8 minutes total.

cd /Users/bradleyneal/forestcity
echo "============================================="
echo " Forest City — Summit County Full Pull"
echo " Danny (Property Managers) + Carla (Referral Partners)"
echo " $(date)"
echo "============================================="
echo ""
echo "Step 1 of 2: Danny — Property Managers..."
echo ""
python3 workers/lead_pipeline.py danny Summit
echo ""
echo "============================================="
echo "Step 2 of 2: Carla — Referral Partners..."
echo ""
python3 workers/lead_pipeline.py carla Summit
echo ""
echo "============================================="
echo "Both pulls complete."
echo "Check logs/activity.log for results."
echo "Summit County deadline: May 31."
echo ""
echo "Press any key to close."
read -n 1
