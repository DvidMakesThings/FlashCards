#!/bin/bash

# Navigate to the project directory
cd ~/FlashCards

# Pull the latest changes from the git repository
git pull origin master

# Run buildozer to build the Android debug package
buildozer -v android debug

# Extract the version from main.py
VERSION=$(grep "__version__" main.py | cut -d "'" -f 2)

# Read the current build number and version from a file, or initialize them if the file doesn't exist
BUILD_INFO_FILE="build_info.txt"
if [ ! -f "$BUILD_INFO_FILE" ]; then
    echo "0" > "$BUILD_INFO_FILE"
    echo "$VERSION" >> "$BUILD_INFO_FILE"
fi
BUILD_NUMBER=$(sed -n '1p' "$BUILD_INFO_FILE")
LAST_VERSION=$(sed -n '2p' "$BUILD_INFO_FILE")

# Check if the version has changed
if [ "$VERSION" != "$LAST_VERSION" ]; then
    BUILD_NUMBER=0
fi

# Increment the build number
BUILD_NUMBER=$((BUILD_NUMBER + 1))

# Save the new build number and version back to the file
echo "$BUILD_NUMBER" > "$BUILD_INFO_FILE"
echo "$VERSION" >> "$BUILD_INFO_FILE"

# Rename the APK file
APK_DIR="bin"
APK_NAME="Wortmeister_v${VERSION}${BUILD_NUMBER}.apk"
mv $APK_DIR/*-debug.apk $APK_DIR/$APK_NAME

# Delete the previous build from the bin folder
rm -f $APK_DIR/*-debug.apk

# Stage all changes
git add .

# Commit the changes
git commit -m "APK autobuilder"

# Push the changes to the repository using the personal access token from the environment variable
git push https://DvidMakesThings:${GITHUB_TOKEN}@github.com/DvidMakesThings/FlashCards.git master

echo "Build and push process completed successfully. APK renamed to $APK_NAME"