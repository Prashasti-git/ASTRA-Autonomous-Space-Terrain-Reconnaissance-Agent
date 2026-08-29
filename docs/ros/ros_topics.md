# ASTRA ROS 2 Topic Reservations

## 1. Standard ROS 2 Reserved Topics

| Topic | Message Type | Description |
| :--- | :--- | :--- |
| `/cmd_vel` | `geometry_msgs/msg/Twist` | Velocity commands to drive motors |
| `/odom` | `nav_msgs/msg/Odometry` | Wheel odometry state |
| `/scan` | `sensor_msgs/msg/LaserScan` | LiDAR point scan data |
| `/imu` | `sensor_msgs/msg/Imu` | Inertial Measurement Unit reading |
| `/camera/image_raw` | `sensor_msgs/msg/Image` | Unprocessed raw camera feed |
| `/camera/depth` | `sensor_msgs/msg/Image` | Depth sensor point map |
| `/tf` | `tf2_msgs/msg/TFMessage` | Dynamic coordinate transforms |
| `/tf_static` | `tf2_msgs/msg/TFMessage` | Static vehicle transforms |

---

## 2. Active ASTRA Custom Topics

| Topic | Message Type | Description |
| :--- | :--- | :--- |
| `/astra/camera/image_raw` | `sensor_msgs/msg/Image` | Simulated/real camera stream from `camera_publisher` |
| `/astra/perception/classification` | `astra_interfaces/msg/Classification` | Perception node classification result (`object_type`, `confidence`, `hazard_level`, `navigation_recommendation`) |
