#!/bin/bash

PROJECT_DIR="/home/animl/internet-speed-monitor"

source $PROJECT_DIR/env/bin/activate &&
cd $PROJECT_DIR/internet-speed-monitor &&
python speedtest.py &&
deactivate