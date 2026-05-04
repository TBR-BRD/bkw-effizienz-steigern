#!/usr/bin/env bash
set -euo pipefail

git init
git remote add origin https://github.com/TBR-BRD/bkw-effizienz-steigern.git
git add .
git commit -m "Initial commit: BKW Effizienzsteigerung"
git branch -M main
git push -u origin main
