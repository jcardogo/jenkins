#! /bin/bash

sudo apt install wireshark
sudo usermod -a -G wireshark acardogo
wireshark 
wireshark --version
sudo usermod -a -G wireshark $USER
sudo chgrp wireshark /usr/bin/dumpcap 
sudo chmod +x /usr/bin/dumpcap 
sudo setcap cap_net_raw,cap_net_admin=eip /usr/bin/dumpcap
wireshark