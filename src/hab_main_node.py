import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HABMainNode(Node):
    """Central orchestrator node for HAB sensors."""
    def __init__(self):
        super().__init__('hab_main_node')
        # Subscribe to topics from sensor nodes
        self.create_subscription(String, 'bmp280/data', self.sensor_callback, 10)
        self.create_subscription(String, 'bosch_pressure/data', self.sensor_callback, 10)
        self.create_subscription(String, 'mcp9600/data', self.sensor_callback, 10)
        self.create_subscription(String, 'gps/data', self.sensor_callback, 10)

    def sensor_callback(self, msg):
        # Placeholder for processing sensor data
        self.get_logger().info(f'Received: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = HABMainNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
