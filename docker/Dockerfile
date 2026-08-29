FROM ros:humble-ros-base

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

SHELL ["/bin/bash", "-c"]

# System dependencies
# System dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-venv \
    python3-colcon-common-extensions \
    git \
    curl \
    build-essential \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Python virtual environment
RUN python3 -m venv --system-site-packages /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Scientific Python packages
RUN pip install --no-cache-dir \
    numpy \
    scipy \
    pandas \
    matplotlib \
    opencv-python

# CPU-only PyTorch (works for both ARM64 and x86_64 Docker hosts)
RUN pip install --no-cache-dir \
    torch \
    torchvision \
    --index-url https://download.pytorch.org/whl/cpu

# Ultralytics
RUN pip install --no-cache-dir ultralytics

# ASTRA workspace
WORKDIR /astra

RUN mkdir -p /astra/ros2_ws/src

# Source ROS 2 automatically
RUN echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc

# Activate Python environment automatically
RUN echo "export PATH=/opt/venv/bin:$PATH" >> /root/.bashrc

CMD ["bash"]