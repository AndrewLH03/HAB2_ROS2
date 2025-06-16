import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from clear_i2c import clear_bus

class MCP9600Node(Node):
    """Publishes thermocouple data from the MCP9600 sensor."""
    def __init__(self):
        super().__init__('mcp9600_node')
        self.publisher = self.create_publisher(String, 'mcp9600/data', 10)
        self.timer = self.create_timer(1.0, self.publish_reading)

    def publish_reading(self):
        try:
            msg = String()
            msg.data = 'mcp9600 sample'
            self.publisher.publish(msg)
        except Exception as e:
            self.get_logger().error(f'Sensor error: {e}, attempting I2C recover')
            clear_bus()


def main(args=None):
    rclpy.init(args=args)
    node = MCP9600Node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
