#!/bin/bash
cd /root/IDS_exportation/
DATE=$(date)
git add .
git commit -m "Rules update: $DATE "
git push origin main
