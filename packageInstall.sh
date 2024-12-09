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
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
check_error "installing required packages"

# Install Python packages
pip3 install --user --upgrade Cython==0.29.33 virtualenv
check_error "installing Python packages"

# Add the following line at the end of your ~/.bashrc file
echo 'export PATH=$PATH:~/.local/bin/' >> ~/.bashrc
check_error "updating ~/.bashrc"

echo "Installation completed successfully."