#!/usr/bin/env bash
# Helper script to build ASTRA ROS 2 workspace inside virtual environment
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

echo "[ASTRA] Sourcing Python venv (/opt/venv) and building ROS 2 workspace..."

if [ -f "/opt/ros/humble/setup.bash" ]; then
    source /opt/ros/humble/setup.bash
fi

if [ -f "/opt/venv/bin/activate" ]; then
    source /opt/venv/bin/activate
fi

cd "${REPO_ROOT}/ros2_ws"
python3 -m colcon build "$@"
echo "[ASTRA] ROS 2 colcon build completed successfully."
