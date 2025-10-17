import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist
import random

class ControllerNode(Node):
    def __init__(self):
        super().__init__('controller_node')
        self.subscriber = self.create_subscription(Range, 'distance', self.distance_callback, 10)
        self.publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.get_logger().info('Vezérlő node elindult.')

    def distance_callback(self, msg):
        twist = Twist()

        if msg.range < 0.3:
            twist.linear.x = 0.0

            # Véletlenszerűen balra vagy jobbra fordul
            if random.random() < 0.5:
                twist.angular.z = 1.0  # balra
                self.get_logger().warn(f'Akadály észlelve ({msg.range:.2f} m) → Fordulás balra')
            else:
                twist.angular.z = -1.0  # jobbra
                self.get_logger().warn(f'Akadály észlelve ({msg.range:.2f} m) → Fordulás jobbra')
        else:
            twist.linear.x = 0.5
            twist.angular.z = 0.0
            self.get_logger().info(f'Szabad út ({msg.range:.2f} m) → Előrehaladás')

        self.publisher.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = ControllerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
