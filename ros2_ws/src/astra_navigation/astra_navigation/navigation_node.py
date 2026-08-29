import rclpy
from rclpy.node import Node

from astra_interfaces.msg import Classification


class NavigationNode(Node):
    """Phase 1 navigation node — reacts to perception's classification output."""

    def __init__(self):
        super().__init__('navigation_node')
        self.subscription = self.create_subscription(
            Classification, '/astra/perception/classification', self.classification_callback, 10)
        self.get_logger().info('Navigation node started — listening on /astra/perception/classification')

    def classification_callback(self, msg: Classification):
        self.get_logger().info(
            f'[ASTRA] Navigation decision for {msg.object_type} '
            f'(confidence {msg.confidence:.2f}, hazard {msg.hazard_level}): '
            f'{msg.navigation_recommendation}')


def main(args=None):
    rclpy.init(args=args)
    node = NavigationNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
