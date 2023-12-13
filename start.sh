#!/bin/bash

echo 'Updating Ubuntu'

apt update && apt upgrade -y

echo 'Ubuntu update complete'

echo 'Attempting to install Wireshark'

apt install -y wireshark

echo 'Installation of Wireshark complete'

echo 'Attempting to install Wireshark Dependencies'

apt install -y tshark

apt install -y rpm

echo 'Installation of Wireshark Dependencies complete'

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

echo 'Attempting to install Python3'

apt install -y python3

echo 'Installation of Python3 complete'

echo 'Attempting to install Python3 Pip'

apt install -y python3-pip

echo 'Installation of Python3 Pip complete'

echo 'Attempting to install boto3'

pip3 install boto3

echo 'Installation of boto3 complete'

echo 'Attempting to install AWS CLI'

pip3 install awscli

echo 'Installation of AWS CLI complete'

echo 'Full Installation of TrafficDetector complete!'

