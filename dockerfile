FROM ubuntu:20.04

# Update and install necessary packages
RUN apt-get update && apt-get install -y \
    git zip unzip sudo openjdk-8-jdk python3-pip python3-setuptools python3-dev patch autoconf automake build-essential libtool pkg-config gettext zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libltdl-dev libssl-dev && \
    apt-get clean

# Install buildozer and other Python dependencies
RUN pip3 install --upgrade buildozer Cython==0.29.33 wheel pip setuptools virtualenv

# Create a non-root user
RUN useradd -m -U builder

# Switch to non-root user
USER builder
WORKDIR /home/builder

# Set up environment
RUN echo "export PATH=$PATH:/home/builder/.local/bin/" >> /home/builder/.profile && \
    echo "export PATH=$PATH:/home/builder/.local/bin/" >> /home/builder/.bashrc

# Set the volume
VOLUME /home/builder/source