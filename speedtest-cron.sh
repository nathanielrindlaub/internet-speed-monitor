#!/bin/bash

PROJECT_DIR = "/home/animl/internet-speed-monitor"

$PROJECT_DIR/env/bin/activate &&
cd $PROJECT_DIR/internet-speed-test &&
python speedtest.py &&
deactivate