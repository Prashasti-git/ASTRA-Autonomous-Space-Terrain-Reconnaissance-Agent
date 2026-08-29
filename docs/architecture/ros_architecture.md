# ASTRA ROS 2 Architecture

## 1. Package Layout
The ASTRA ROS 2 workspace (`ros2_ws/src`) is structured as follows:

| Package | Type | Description |
| :--- | :--- | :--- |
| `astra_interfaces` | CMake / rosidl | Custom ROS 2 messages (`Classification.msg`, `RoverState.msg`, `MissionState.msg`, `Hazard.msg`, etc.) |
| `astra_sensors` | Python (`ament_python`) | Simulated camera publisher node (`camera_publisher.py`) emitting `/astra/camera/image_raw` |
| `astra_perception` | Python (`ament_python`) | Vision processing node (`perception_node.py`) classifying terrain features (`ROCK`, `CRATER`, `UNKNOWN`) |
| `astra_navigation` | Python (`ament_python`) | Reactive navigation node (`navigation_node.py`) processing classifications into velocity/steering output |
| `astra_bringup` | Python (`ament_python`) | System launch orchestration (`astra_demo.launch.py`) launching sensors, perception, and navigation |
| `astra_simulation` | Skeleton | Reserved for Gazebo / Isaac Sim bridge |
| `astra_classification` | Skeleton | Reserved for deep ML classification nodes |
| `astra_mission` | Skeleton | Reserved for ROS 2 action server mission controller |

---

## 2. Topic Dataflow
```
[ camera_publisher ]
        │
        │  /astra/camera/image_raw (sensor_msgs/msg/Image)
        ▼
[ perception_node ]
        │
        │  /astra/perception/classification (astra_interfaces/msg/Classification)
        ▼
[ navigation_node ]
        │
        │  /cmd_vel (geometry_msgs/msg/Twist)
        ▼
[ Rover Drive Actuators / Simulation ]
```
