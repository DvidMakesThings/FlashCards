#!/bin/bash

# Function to check the exit status of the last command and print an error message if it failed
check_error() {
    if [ $? -ne 0 ]; then
        echo -e "\e[31mError occurred during: $1\e[0m"
        read -p "Press any key to continue..."
        exit 1
    fi
}

# Navigate to the project directory
cd ~/FlashCards
check_error "navigating to project directory"

# Pull the latest changes from the git repository
git pull origin master
check_error "pulling latest changes from git"

# Run buildozer to build the Android debug package
buildozer -v android debug
check_error "running buildozer"

# Commit the changes
git commit -m "Update APK after successful build"
check_error "committing changes"

# Push the changes to the repository
git push origin main
check_error "pushing changes to git repository"

echo "Build and push process completed successfully."