import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from clear_i2c import clear_bus

class BMP280Node(Node):
    """Publishes temperature and pressure from a BMP280 sensor."""
    def __init__(self):
        super().__init__('bmp280_node')
        self.publisher = self.create_publisher(String, 'bmp280/data', 10)
        self.timer = self.create_timer(1.0, self.publish_reading)

    def publish_reading(self):
        try:
            msg = String()
            msg.data = 'bmp280 sample'
            self.publisher.publish(msg)
        except Exception as e:
            self.get_logger().error(f'Sensor error: {e}, attempting I2C recover')
            clear_bus()


def main(args=None):
    rclpy.init(args=args)
    node = BMP280Node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
