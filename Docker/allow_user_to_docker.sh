#!/bin/bash

#Allow user to run docker commands
sudo docker --version
systemctl status docker
sudo usermod -aG docker $USER
newgrp docker
su - $USER
sudo reboot
