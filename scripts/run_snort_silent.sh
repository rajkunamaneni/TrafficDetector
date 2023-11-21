#!/bin/bash

# Starting Snort comment 
echo "Starting Snort"

# Start Snort in background
sudo snort -q -l /var/log/snort -i wlan0 -A console -c /etc/snort/snort.conf &

