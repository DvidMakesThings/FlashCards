#!/bin/bash

# Update and upgrade the system
sudo apt update && sudo apt upgrade -y

# Install git
sudo apt-get install -y git

# Clone the buildozer repository
git clone https://github.com/kivy/buildozer.git

# Install Python and pip
sudo apt install -y python3 python3-pip ipython3

# Install Cython
sudo pip3 install cython==0.29.37

# Install autoconf
sudo apt-get install -y autoconf

# Install OpenJDK 8
sudo apt-get install -y openjdk-8-jdk

# Install build essentials and other dependencies
sudo apt install -y build-essential libltdl-dev libffi-dev libssl-dev python-dev-is-python3

# Install unzip and zip
sudo apt-get install -y unzip zip

# Upgrade Cython
sudo pip3 install --upgrade cython

# Install Python 3.12 virtual environment
sudo apt install -y python3.12-venv

# Navigate to the buildozer directory and install it
cd buildozer/
sudo python3 setup.py install

# Navigate to the home directory
cd ~

# Clone the FlashCards project
git clone https://github.com/DvidMakesThings/FlashCards.git

# Navigate to the FlashCards directory
cd FlashCards/