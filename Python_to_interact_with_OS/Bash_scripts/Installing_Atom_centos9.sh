#!/bin/bash

# Update package list
sudo dnf update -y

# Install required dependencies
sudo dnf install -y epel-release
sudo dnf install -y gcc-c++
sudo dnf install -y git

# Install Atom
sudo dnf install -y atom

# Optional: Install Atom packages
apm install minimap
apm install file-icons
apm install language-python

# Launch Atom
atom &