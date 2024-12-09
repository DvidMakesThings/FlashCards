# Base image with Python 3.9 (you can change the version as needed)
FROM ubuntu:20.04

# Set environment variables
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Install dependencies
RUN apt-get update && apt-get install -y \
    git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config \
    zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev \
    && apt-get clean

# Upgrade pip and install required Python packages
RUN pip3 install --no-cache-dir --upgrade \
    Cython==0.29.33 virtualenv buildozer

# Add Python's local bin directory to PATH
ENV PATH="$PATH:/root/.local/bin"

# Set working directory in the container
WORKDIR /app

# Copy project files into the container
COPY . /app

# Command to build APK
CMD ["buildozer", "android", "debug"]
