#!/bin/bash
set -x  # echo on
sudo mount -o remount,rw /
sudo pkill -f app.py  # Ukončí předchozí instanci app.py (pokud existuje)
sudo pkill -f motion_detection.py
sudo pkill -f bme.py
sudo pkill -f graf.py
python3 /opt/camera_stream/LEDoff.py
python3 /opt/camera_stream/graf.py
/opt/camera_stream/set-time.sh
nohup python3 /opt/camera_stream/bme.py & # načíta hodnoty z BME
python3 /opt/camera_stream/app.py  # Spustí aplikaci app.py
