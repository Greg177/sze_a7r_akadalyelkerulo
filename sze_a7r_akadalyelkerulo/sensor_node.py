import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range
import random

class SensorNode(Node):
    def __init__(self):
        super().__init__('sensor_node')
        self.publisher_ = self.create_publisher(Range, 'distance', 10)
        self.timer = self.create_timer(0.5, self.publish_distance)
        self.get_logger().info('Szenzor node elindult.')

    def publish_distance(self):
        msg = Range()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.range = random.uniform(0.05, 2.0)  # 5 cm – 2 m között
        self.publisher_.publish(msg)
        self.get_logger().info(f'💡 Távolság: {msg.range:.2f} m')

def main(args=None):
    rclpy.init(args=args)
    node = SensorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
