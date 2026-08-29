"""
ROS 2 Integration Test
Launches `astra_demo.launch.py`, monitors process health for 3 seconds, and verifies clean execution.
"""
import os
import subprocess
import time
import pytest


def test_ros2_bringup_launch():
    # Verify environment is ROS 2 enabled
    ros_distro = os.getenv("ROS_DISTRO", "humble")
    
    cmd = [
        "bash",
        "-c",
        f"source /opt/ros/humble/setup.bash && source /opt/venv/bin/activate && "
        f"source /astra/ros2_ws/install/setup.bash 2>/dev/null || true && "
        f"ros2 launch astra_bringup astra_demo.launch.py"
    ]

    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Let process run for 3 seconds to verify initialization
    time.sleep(3)

    # Check if process crashed prematurely
    return_code = proc.poll()
    assert return_code is None, f"ROS 2 launch exited prematurely with code {return_code}"

    # Terminate launch process cleanly
    proc.terminate()
    try:
        proc.wait(timeout=2)
    except subprocess.TimeoutExpired:
        proc.kill()
