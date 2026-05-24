#!/bin/bash
# Double-click this file in Finder to run the full Medina County pull.
# Runs BOTH Danny (property managers) AND Carla (referral partners) for Medina County.
# No typing required. Takes 5-8 minutes total.

cd /Users/bradleyneal/forestcity
echo "============================================="
echo " Forest City — Medina County Full Pull"
echo " Danny (Property Managers) + Carla (Referral Partners)"
echo " $(date)"
echo "============================================="
echo ""
echo "Step 1 of 2: Danny — Property Managers..."
echo ""
python3 workers/lead_pipeline.py danny Medina
echo ""
echo "============================================="
echo "Step 2 of 2: Carla — Referral Partners..."
echo ""
python3 workers/lead_pipeline.py carla Medina
echo ""
echo "============================================="
echo "Both pulls complete."
echo "Check logs/activity.log for results."
echo "Medina County: Week 22 (June 1)."
echo ""
echo "Press any key to close."
read -n 1
