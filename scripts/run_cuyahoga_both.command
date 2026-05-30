#!/bin/bash
# Double-click this file in Finder to run the full Cuyahoga County pull.
# Runs BOTH Danny (property managers + 51 commercial segments) AND Carla (referral partners).
# June 8 (Week 24) — Cleveland, Parma, Lakewood, Strongsville, Beachwood. BIGGEST pull of the year.
# No typing required. Takes 12-20 minutes total.

cd /Users/bradleyneal/forestcity
echo "============================================="
echo " Forest City — Cuyahoga County Full Pull"
echo " Danny (PM + 51 Commercial Segments) + Carla (Referral Partners)"
echo " $(date)"
echo "============================================="
echo ""
echo "Step 1 of 2: Danny — Property Managers + All Commercial Segments..."
echo "This uses title + org keyword batching across 51+ segments."
echo "Will take 8-15 minutes. Let it run."
echo ""
python3 workers/lead_pipeline.py danny Cuyahoga
echo ""
echo "============================================="
echo "Step 2 of 2: Carla — Referral Partners..."
echo ""
python3 workers/lead_pipeline.py carla Cuyahoga
echo ""
echo "============================================="
echo "Both pulls complete."
echo "Check logs/activity.log for results."
echo "Cuyahoga County: Week 24 (June 8) — Largest market."
echo ""
echo "Press any key to close."
read -n 1
