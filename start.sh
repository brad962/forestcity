#!/bin/bash
# Forest City AI Office — start the dashboard server
cd "$(dirname "$0")"
echo ""
echo "  Forest City AI Office"
echo "  Starting dashboard at http://localhost:3737/dashboard.html"
echo ""
python3 server.py
