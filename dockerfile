# Use Ubuntu 18.04 as the base image
FROM ubuntu:18.04

# Set environment variables for non-interactive installs
ENV DEBIAN_FRONTEND=noninteractive
ENV ANDROID_HOME=/opt/android-sdk
ENV PATH="${ANDROID_HOME}/cmdline-tools/latest/bin:${ANDROID_HOME}/platform-tools:${PATH}"
ENV BUILD_PATH=/app/.buildozer  

# Install required packages including libstdc++6, Flutter dependencies, and Android SDK dependencies
RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-venv wget unzip git zlib1g-dev cmake autoconf automake libtool libffi-dev openjdk-11-jdk build-essential libstdc++6 curl && \
    apt-get clean

# Install Buildozer and Cython
RUN pip3 install buildozer cython && \
    mkdir -p /root/.local/bin && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    echo 'export PATH=$HOME/.local/bin:$PATH' >> /root/.bashrc

# Install expect
RUN apt-get update && apt-get install -y expect

# Install the command-line tools
RUN mkdir -p ${ANDROID_HOME}/cmdline-tools && \
    wget -q https://dl.google.com/android/repository/commandlinetools-linux-9477386_latest.zip -O cmdline-tools.zip && \
    unzip -q cmdline-tools.zip -d ${ANDROID_HOME}/cmdline-tools && \
    mv ${ANDROID_HOME}/cmdline-tools/cmdline-tools ${ANDROID_HOME}/cmdline-tools/latest && \
    rm cmdline-tools.zip

# Accept licenses using yes (IMPORTANT)
RUN yes | sdkmanager --licenses

# Install SDK components
RUN sdkmanager "platform-tools" "build-tools;33.0.2" "platforms;android-33"  # Or your desired versions

# Manually accept the android-sdk-preview-license
RUN mkdir -p ${ANDROID_HOME}/licenses && \
    echo "8933bad161af4178b1185d1a37fbf41ea5269c55" > ${ANDROID_HOME}/licenses/android-sdk-license && \
    echo "d56f5187479451eabf01fb78af6dfcb131a6481e" > ${ANDROID_HOME}/licenses/android-sdk-preview-license

# Install Flutter SDK
RUN git clone https://github.com/flutter/flutter.git /opt/flutter && \
    /opt/flutter/bin/flutter doctor

# Automatically accept all Android SDK licenses using yes
RUN yes | /opt/flutter/bin/flutter doctor --android-licenses

# Create a non-root user for running Buildozer
RUN useradd -m builder && mkdir -p /app && chown -R builder:builder /app

# Switch to non-root user
USER builder

# Set working directory
WORKDIR /app

# Default command to build the APK with Buildozer and run Flutter
CMD ["sh", "-c", "buildozer android debug && /opt/flutter/bin/flutter run"]