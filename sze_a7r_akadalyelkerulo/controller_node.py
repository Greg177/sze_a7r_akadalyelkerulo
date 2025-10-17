import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist
import random
from turtlesim.msg import Pose

class ControllerNode(Node):
    def __init__(self):
        super().__init__('controller_node')

        self.subscriber = self.create_subscription(Range, 'distance', self.distance_callback, 10)
        self.pose_sub = self.create_subscription(Pose, 'turtle1/pose', self.pose_callback, 10)
        self.publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)

        self.turning_direction = 0
        self.pose = None

        self.get_logger().info('Vezérlő node elindult.')

    def pose_callback(self, msg):
        self.pose = msg

    def distance_callback(self, msg):
        twist = Twist()

        if self.pose is None:
            return


        min_x, max_x = 0.5, 10.5
        min_y, max_y = 0.5, 10.5


        if msg.range < 0.3:
            twist.linear.x = 0.0

            if self.turning_direction == 0:
                self.turning_direction = 1 if random.random() < 0.5 else -1

            twist.angular.z = 1.0 * self.turning_direction
            direction_str = 'balra' if self.turning_direction == 1 else 'jobbra'
            self.get_logger().warn(f'Akadály észlelve ({msg.range:.2f} m) → Fordulás {direction_str}')

        else:
            twist.linear.x = 0.5
            twist.angular.z = 0.0
            self.turning_direction = 0
            self.get_logger().info(f'Szabad út ({msg.range:.2f} m) → Előrehaladás')


        if self.pose.x < min_x:
            twist.linear.x = 0.0
            twist.angular.z = 1.0
        elif self.pose.x > max_x:
            twist.linear.x = 0.0
            twist.angular.z = -1.0
        if self.pose.y < min_y:
            twist.linear.x = 0.0
            twist.angular.z = 1.0
        elif self.pose.y > max_y:
            twist.linear.x = 0.0
            twist.angular.z = -1.0

        self.publisher.publish(twist)


def main(args=None):
    rclpy.init(args=args)
    node = ControllerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
