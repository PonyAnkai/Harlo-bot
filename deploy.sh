#!/bin/bash
set -e

echo "[1] Pull last-version"
cd /var/www/bot-harlo
git fetch origin
git reset --hard origin/master

echo "[2] Setup requirements"
pip install -r requirements.txt

echo "[3] Restart site ponyglory.ru"
sudo systemctl restart ponyglory
