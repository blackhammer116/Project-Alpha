#!/usr/bin/env bash
# This script is used to configure a new machine
# with all the necessary security tools
# This is ONLY to people with other than kali debian
sudo apt-get update
sudo apt-get install net-tools
sudo apt-get install nmap
wget ‘https://github.com/sqlmapproject/sqlmap/tarball/master’ –output-document=sqlmap.tar.gz
tar -xvf sqlmap.tar.gz
