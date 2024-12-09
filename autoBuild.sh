#!/bin/bash

# Navigate to the project directory
cd ~/FlashCards

# Pull the latest changes from the git repository
git pull origin master

# Run buildozer to build the Android debug package
buildozer -v android debug

# Extract the version from main.py
VERSION=$(grep "__version__" main.py | cut -d "'" -f 2)

# Read the current build number from a file, or initialize it to 0 if the file doesn't exist
BUILD_NUMBER_FILE="build_number.txt"
if [ ! -f "$BUILD_NUMBER_FILE" ]; then
    echo "0" > "$BUILD_NUMBER_FILE"
fi
BUILD_NUMBER=$(cat "$BUILD_NUMBER_FILE")

# Increment the build number
BUILD_NUMBER=$((BUILD_NUMBER + 1))

# Save the new build number back to the file
echo "$BUILD_NUMBER" > "$BUILD_NUMBER_FILE"

# Rename the APK file
APK_DIR="bin"
APK_NAME="Wortmeister_v${VERSION}${BUILD_NUMBER}.apk"
mv $APK_DIR/*-debug.apk $APK_DIR/$APK_NAME

# Stage all changes
git add .

# Commit the changes
git commit -m "APK autobuilder"

# Push the changes to the repository using the personal access token from the environment variable
git push https://DvidMakesThings:${GITHUB_TOKEN}@github.com/DvidMakesThings/FlashCards.git master

echo "Build and push process completed successfully."