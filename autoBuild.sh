#!/bin/bash

# Navigate to the project directory
cd ~/FlashCards

# Pull the latest changes from the git repository
git pull origin master

# Run buildozer to build the Android debug package
buildozer -v android debug

# Stage all changes
git add .

# Commit the changes
git commit -m "APK autobuilder"

# Push the changes to the repository using the personal access token from the environment variable
git push https://DvidMakesThings:${GITHUB_TOKEN}@github.com/DvidMakesThings/FlashCards.git master

echo "Build and push process completed successfully."