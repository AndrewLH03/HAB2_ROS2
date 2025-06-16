import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from clear_i2c import clear_bus

class BoschPressureNode(Node):
    """Publishes pressure data from a Bosch sensor."""
    def __init__(self):
        super().__init__('bosch_pressure_node')
        self.publisher = self.create_publisher(String, 'bosch_pressure/data', 10)
        self.timer = self.create_timer(1.0, self.publish_reading)

    def publish_reading(self):
        try:
            msg = String()
            msg.data = 'bosch pressure sample'
            self.publisher.publish(msg)
        except Exception as e:
            self.get_logger().error(f'Sensor error: {e}, attempting I2C recover')
            clear_bus()


def main(args=None):
    rclpy.init(args=args)
    node = BoschPressureNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
