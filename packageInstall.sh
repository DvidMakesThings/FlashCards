#!/bin/bash

# Function to check the exit status of the last command and print an error message if it failed
check_error() {
    if [ $? -ne 0 ]; then
        echo -e "\e[31mError occurred during: $1\e[0m"
        read -p "Press any key to continue..."
        exit 1
    fi
}

# Update the system
sudo apt update
check_error "system update"

# Install required packages
sudo apt install -y git zip unzip openjdk-17-jdk python3.9 python3.9-dev autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
check_error "installing required packages"

# Upgrade pip for Python 3.9
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python3.9 get-pip.py
check_error "upgrading pip"

# Install Python packages globally
pip3.9 install --upgrade Cython==0.29.33 virtualenv buildozer
check_error "installing Python packages"

# Add the following line at the end of your ~/.bashrc file
echo 'export PATH=$PATH:~/.local/bin/' >> ~/.bashrc
check_error "updating ~/.bashrc"

# Source the ~/.bashrc file to update the PATH for the current session
source ~/.bashrc
check_error "sourcing ~/.bashrc"

# Navigate to the home directory
cd ~
check_error "navigating to home directory"

# Clone the FlashCards repository
git clone https://github.com/DvidMakesThings/FlashCards.git
check_error "cloning FlashCards repository"

# Navigate to the FlashCards directory
cd FlashCards
check_error "navigating to FlashCards directory"

