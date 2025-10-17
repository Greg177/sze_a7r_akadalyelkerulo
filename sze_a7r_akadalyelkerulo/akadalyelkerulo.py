#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan  
from geometry_msgs.msg import Twist

class Akadalyelkerulo(Node):
    def __init__(self):
        super().__init__('akadalyelkerulo')

        # Publisher a robot mozgására
        self.cmd_pub = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)


        # Subscriber a LiDAR adatokhoz
        self.scan_sub = self.create_subscription(
            LaserScan,
            'scan',
            self.scan_callback,
            10
        )

        self.get_logger().info('Akadalyelkerulo node elindult!')

    def scan_callback(self, msg: LaserScan):

        min_distance = min(msg.ranges) if msg.ranges else float('inf')

        twist = Twist()
        if min_distance < 0.5:
            twist.linear.x = 0.0
            twist.angular.z = 0.5 
            self.get_logger().info(f'Akadály észlelve: {min_distance:.2f} m, fordulás!')
        else:
            twist.linear.x = 0.5
            twist.angular.z = 0.0
            self.get_logger().info(f'Utó megtisztítva, haladás: {min_distance:.2f} m')

        self.cmd_pub.publish(twist)


def main(args=None):
    rclpy.init(args=args)
    node = Akadalyelkerulo()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
