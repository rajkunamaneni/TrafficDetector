#!/bin/bash

echo 'Updating Ubuntu'

apt update && apt upgrade -y

echo 'Ubuntu update complete'

echo 'Attempting to install Wireshark'

apt install -y wireshark

echo 'Installation of Wireshark complete'

echo 'Attempting to install Snort'

apt install -y snort

echo 'Installation of Snort complete'

echo 'Attempting to install Nmap'

apt install -y nmap

nmap --version

echo 'Installation of Nmap complete'

echo 'Attempting to install Fping'

apt install -y fping

echo 'Installation of Fping complete'

echo 'Full Installation of TrafficDetector complete!'

