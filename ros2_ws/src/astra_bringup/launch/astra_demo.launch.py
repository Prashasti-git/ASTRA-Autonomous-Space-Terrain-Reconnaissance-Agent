from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(package='astra_sensors', executable='camera_publisher',
             name='camera_publisher', output='screen'),
        Node(package='astra_perception', executable='perception_node',
             name='perception_node', output='screen'),
        Node(package='astra_navigation', executable='navigation_node',
             name='navigation_node', output='screen'),
    ])
