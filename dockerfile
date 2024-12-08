# Use Ubuntu 18.04 as the base image
FROM ubuntu:18.04

# Set environment variables for non-interactive installs
ENV DEBIAN_FRONTEND=noninteractive
ENV ANDROID_HOME=/opt/android-sdk
ENV PATH="${ANDROID_HOME}/cmdline-tools/latest/bin:${ANDROID_HOME}/platform-tools:${PATH}"
ENV BUILD_PATH=/app/.buildozer  


# Install required packages
RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-venv wget unzip git zlib1g-dev cmake autoconf automake libtool libffi-dev openjdk-11-jdk && \
    apt-get clean

# Install Buildozer and Cython
RUN pip3 install buildozer cython && \
    mkdir -p /root/.local/bin && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    echo 'export PATH=$HOME/.local/bin:$PATH' >> /root/.bashrc

# Install Android SDK command-line tools
RUN mkdir -p ${ANDROID_HOME}/cmdline-tools && \
    wget -q https://dl.google.com/android/repository/commandlinetools-linux-8512546_latest.zip -O cmdline-tools.zip && \
    unzip -q cmdline-tools.zip -d ${ANDROID_HOME}/cmdline-tools && \
    mv ${ANDROID_HOME}/cmdline-tools/cmdline-tools ${ANDROID_HOME}/cmdline-tools/latest && \
    rm cmdline-tools.zip && \
    yes | sdkmanager --licenses && \
    sdkmanager --update && \
    yes | sdkmanager --licenses && \
    yes | sdkmanager "platform-tools" "build-tools;33.0.0" "platforms;android-33"

# Create a non-root user for running Buildozer
RUN useradd -m builder && mkdir -p /app && chown -R builder:builder /app

# Switch to non-root user
USER builder

# Set working directory
WORKDIR /app

# Default command
CMD ["buildozer", "android", "debug"]
