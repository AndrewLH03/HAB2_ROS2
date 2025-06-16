import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class StatusNode(Node):
    """Aggregates readings from multiple sensors."""
    def __init__(self):
        super().__init__('status_node')
        self.data = {}
        self.create_subscription(String, 'bmp280/data', self.update_bmp280, 10)
        self.create_subscription(String, 'bosch_pressure/data', self.update_bosch, 10)
        self.create_subscription(String, 'mcp9600/data', self.update_mcp9600, 10)
        self.timer = self.create_timer(5.0, self.report_status)

    def update_bmp280(self, msg):
        self.data['bmp280'] = msg.data

    def update_bosch(self, msg):
        self.data['bosch_pressure'] = msg.data

    def update_mcp9600(self, msg):
        self.data['mcp9600'] = msg.data

    def report_status(self):
        self.get_logger().info(f"Status: {self.data}")


def main(args=None):
    rclpy.init(args=args)
    node = StatusNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
