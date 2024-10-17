#!/bin/bash
set -x  # echo on
sudo mount -o remount,rw /
sudo pkill -f app.py  # Ukončí předchozí instanci app.py (pokud existuje)
sudo pkill -f motion_detection.py
python3 /opt/camera_stream/LEDm.py
/opt/camera_stream/set-time.sh
python3 /opt/camera_stream/app.py  # Spustí aplikaci app.py
