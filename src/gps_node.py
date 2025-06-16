import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class GPSNode(Node):
    """Publishes GPS data."""
    def __init__(self):
        super().__init__('gps_node')
        self.publisher = self.create_publisher(String, 'gps/data', 10)
        self.timer = self.create_timer(1.0, self.publish_reading)

    def publish_reading(self):
        msg = String()
        msg.data = 'gps sample'
        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = GPSNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
