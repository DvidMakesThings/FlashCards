FROM python:3.11.8-bookworm

# Create a non-root user and install necessary packages
RUN useradd -m -U builder && \
    apt update && \
    apt install -y git zip unzip sudo openjdk-17-jdk python3-pip python3-setuptools python3-dev patch autoconf automake build-essential libtool pkg-config gettext zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libltdl-dev libssl-dev && \
    apt remove -y ccache && \
    apt clean

# Switch to non-root user
USER builder
WORKDIR /home/builder

# Set up environment and install dependencies
RUN echo "export PATH=$PATH:/home/builder/.local/bin/" >> /home/builder/.profile && \
    echo "export PATH=$PATH:/home/builder/.local/bin/" >> /home/builder/.bashrc && \
    pip3 install --user --upgrade buildozer Cython==0.29.33 wheel pip setuptools virtualenv && \
    git clone https://github.com/kivy/python-for-android.git

# Set the volume
VOLUME /home/builder/source