import random

import cv2
import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image


class CameraPublisher(Node):
    """Simulates a rover camera by publishing synthetic frames."""

    WIDTH = 320
    HEIGHT = 240

    def __init__(self):
        super().__init__('camera_publisher')
        self.publisher_ = self.create_publisher(Image, '/astra/camera/image_raw', 10)
        self.timer = self.create_timer(2.0, self.publish_frame)
        self.get_logger().info('Camera publisher started — publishing to /astra/camera/image_raw')

    def generate_frame(self):
        frame = np.full((self.HEIGHT, self.WIDTH, 3), 180, dtype=np.uint8)
        scenario = random.choice(['crater', 'rock', 'unknown', 'empty'])

        if scenario == 'crater':
            center = (random.randint(80, self.WIDTH - 80), random.randint(60, self.HEIGHT - 60))
            radius = random.randint(30, 60)
            cv2.circle(frame, center, radius, (40, 40, 40), -1)
        elif scenario == 'rock':
            x, y = random.randint(40, self.WIDTH - 100), random.randint(40, self.HEIGHT - 100)
            w, h = random.randint(40, 70), random.randint(40, 70)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (200, 200, 200), -1)
        elif scenario == 'unknown':
            noise = np.random.randint(0, 255, (self.HEIGHT, self.WIDTH, 3), dtype=np.uint8)
            frame = cv2.addWeighted(frame, 0.4, noise, 0.6, 0)

        return frame

    def publish_frame(self):
        frame = self.generate_frame()
        msg = Image()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'camera_link'
        msg.height = self.HEIGHT
        msg.width = self.WIDTH
        msg.encoding = 'bgr8'
        msg.is_bigendian = 0
        msg.step = self.WIDTH * 3
        msg.data = frame.tobytes()
        self.publisher_.publish(msg)
        self.get_logger().info('Published camera frame')


def main(args=None):
    rclpy.init(args=args)
    node = CameraPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
