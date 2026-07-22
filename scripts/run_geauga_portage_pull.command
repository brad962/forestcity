#!/bin/bash
# Double-click this file in Finder to run the Geauga+Portage County lead pull (Danny only).
# July 2026 (Week 30) — Chardon, Chesterland, Burton, Aurora, Ravenna, Kent, Streetsboro.
# High-value: Grand River Marina, Debonne/Laurello Vineyards, Fowler's Mill, 200+ nurseries,
# Willoughby Hopkins FBO, rubber/elastomer mfg, wire/cable mfg, precast concrete plants.
# No typing required. Takes 8-12 minutes.

cd /Users/bradleyneal/forestcity
echo "=============================================="
echo " Forest City — Geauga + Portage County Lead Pull"
echo " $(date)"
echo "=============================================="
echo ""
echo "Pulling Geauga+Portage County leads from Apollo..."
echo "NOTE: Only county in the 6-county rotation not yet pulled."
echo "      214 commercial segments queued — including marinas, wineries, golf courses,"
echo "      wholesale nurseries (Geauga = Ohio nursery heartland), manufacturing corridor."
echo "This run will take 8-12 minutes — let it run unattended."
echo ""
python3 workers/lead_pipeline.py danny "Geauga+Portage"
echo ""
echo "=============================================="
echo "Done. Check logs/activity.log for results."
echo "Press any key to close."
read -n 1
