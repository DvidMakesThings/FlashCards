# Use Ubuntu 20.04 as the base image (more recent and better support)
FROM ubuntu:20.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV ANDROID_HOME=/opt/android-sdk
ENV PATH="${ANDROID_HOME}/cmdline-tools/latest/bin:${ANDROID_HOME}/platform-tools:${PATH}"

# Install essential packages
RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-venv wget unzip git zlib1g-dev cmake autoconf automake libtool libffi-dev openjdk-11-jdk build-essential libstdc++6 curl zip && \
    apt-get clean

# Install Buildozer, Cython
RUN pip3 install buildozer cython

# Android SDK Command-line tools (version 9695651)
RUN mkdir -p ${ANDROID_HOME}/cmdline-tools && \
    wget -q https://dl.google.com/android/repository/commandlinetools-linux-9695651.zip -O cmdline-tools.zip && \
    unzip -q cmdline-tools.zip -d ${ANDROID_HOME}/cmdline-tools && \
    mv ${ANDROID_HOME}/cmdline-tools/cmdline-tools ${ANDROID_HOME}/cmdline-tools/latest && \
    rm cmdline-tools.zip

# Accept licenses - crucial change: use `expect` for reliable license acceptance
RUN apt-get install -y expect && \
    expect -c 'spawn sdkmanager --licenses; expect { \
        "y/n" { send "y\r"; exp_continue } \
        eof { exit 0 } \
    }'

# Install SDK components (matching versions)
RUN sdkmanager --update && \
    sdkmanager "platform-tools" "build-tools;33.0.2" "platforms;android-33"

# Create buildozer user and set permissions
RUN useradd -m builder && mkdir -p /app && chown -R builder:builder /app
USER builder
WORKDIR /app

# CMD - removed flutter, focus on buildozer
CMD ["buildozer", "android", "debug"]
