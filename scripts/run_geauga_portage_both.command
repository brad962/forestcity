#!/bin/bash
# Double-click this file in Finder to run the full Geauga+Portage County pull.
# Runs BOTH Danny (property managers + commercial segments) AND Carla (referral partners).
# July 2026 (Week 30) — Chardon, Chesterland, Burton, Aurora, Ravenna, Kent, Streetsboro.
# High-value targets: Grand River Marina, Debonne/Laurello Vineyards, Fowler's Mill Golf Course,
# Aurora Country Club, Geauga wholesale nurseries (200+ operations), Willoughby Hopkins FBO,
# Parker Hannifin/Freudenberg-NOK Twinsburg, rubber/elastomer plants, wire/cable mfg.
# No typing required. Takes 12-20 minutes total — run unattended.

cd /Users/bradleyneal/forestcity
echo "============================================="
echo " Forest City — Geauga + Portage County Pull"
echo " Danny (Property Managers) + Carla (Referral Partners)"
echo " $(date)"
echo "============================================="
echo ""
echo "Step 1 of 2: Danny — Property Managers + 214 Commercial Segments..."
echo "This is the ONLY county in the 6-county rotation not yet pulled."
echo "Expect 12-20 minutes — run unattended."
echo ""
python3 workers/lead_pipeline.py danny "Geauga+Portage"
echo ""
echo "============================================="
echo "Step 2 of 2: Carla — Referral Partners..."
echo ""
python3 workers/lead_pipeline.py carla "Geauga+Portage"
echo ""
echo "============================================="
echo "Both pulls complete."
echo "Check logs/activity.log for results."
echo "Geauga+Portage: Week 30 — marinas, vineyards, nurseries, manufacturing corridor."
echo ""
echo "Press any key to close."
read -n 1
