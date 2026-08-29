import cv2
import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

from astra_interfaces.msg import Classification


class PerceptionNode(Node):
    """Phase 1 perception + classification pipeline."""

    CONFIDENCE_THRESHOLD = 0.6

    def __init__(self):
        super().__init__('perception_node')
        self.subscription = self.create_subscription(
            Image, '/astra/camera/image_raw', self.image_callback, 10)
        self.publisher_ = self.create_publisher(
            Classification, '/astra/perception/classification', 10)
        self.get_logger().info('Perception node started — listening on /astra/camera/image_raw')

    def image_callback(self, msg: Image):
        frame = np.frombuffer(msg.data, dtype=np.uint8).reshape(msg.height, msg.width, 3)
        self.get_logger().info('[ASTRA] Camera frame received')

        result = self.detect_and_classify(frame)
        if result is None:
            return

        object_type, confidence, hazard, nav = result

        self.get_logger().info('[ASTRA] Object detected')
        self.get_logger().info(
            f'[ASTRA] Classification:\n        Type: {object_type}\n'
            f'        Confidence: {confidence:.2f}\n        Hazard: {hazard}')
        self.get_logger().info(f'[ASTRA] Navigation recommendation:\n        {nav}')

        out = Classification()
        out.object_type = object_type
        out.confidence = confidence
        out.hazard_level = hazard
        out.navigation_recommendation = nav
        self.publisher_.publish(out)

    def detect_and_classify(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if not contours:
            return None

        largest = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest)
        if area < 200:
            return None

        perimeter = cv2.arcLength(largest, True)
        circularity = 4 * np.pi * area / (perimeter ** 2) if perimeter > 0 else 0
        approx = cv2.approxPolyDP(largest, 0.04 * perimeter, True)

        if circularity > 0.75:
            object_type = 'CRATER'
            confidence = min(0.95, 0.6 + circularity * 0.3)
        elif len(approx) == 4:
            object_type = 'ROCK'
            confidence = min(0.95, 0.55 + (1 - abs(circularity - 0.5)) * 0.3)
        else:
            object_type = 'UNKNOWN'
            confidence = 0.4

        if confidence < self.CONFIDENCE_THRESHOLD:
            object_type = 'UNKNOWN'

        if object_type == 'CRATER':
            hazard, nav = 'HIGH', 'AVOID'
        elif object_type == 'ROCK':
            hazard, nav = 'LOW', 'PASSABLE'
        else:
            hazard, nav = 'HIGH', 'AVOID — record for analysis'

        return object_type, float(confidence), hazard, nav


def main(args=None):
    rclpy.init(args=args)
    node = PerceptionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
