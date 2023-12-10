#!/bin/bash

echo 'Updating Ubuntu'

apt update && apt upgrade -y

echo 'Ubuntu update complete'

echo 'Attempting to install Wireshark'

apt install wireshark

echo 'Installation of Wireshark complete'

echo 'Attempting to install Snort'

apt install snort

echo 'Installation of Snort complete'

echo 'Attempting to install Nmap'

apt install -y nmap

nmap --version

echo 'Installation of Nmap complete'

echo 'Attempting to install Fping'

apt install fping

echo 'Installation of Fping complete'

