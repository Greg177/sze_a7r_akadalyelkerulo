import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist
import random
from turtlesim.msg import Pose

class ControllerNode(Node):
    def __init__(self):
        super().__init__('controller_node')

        # Subscribers
        self.sub_distance = self.create_subscription(Range, 'distance', self.distance_callback, 10)
        self.sub_pose = self.create_subscription(Pose, 'turtle1/pose', self.pose_callback, 10)

        # Publisher
        self.pub_cmd = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)

        
        self.state = "forward"          
        self.turning_direction = 0      
        self.pose = None

        
        self.min_distance = 0.3
        self.linear_speed = 0.5
        self.angular_speed = 1.0
        self.min_x, self.max_x = 0.5, 10.5
        self.min_y, self.max_y = 0.5, 10.5

        self.get_logger().info('Vezérlő node elindult.')

    def pose_callback(self, msg):
        self.pose = msg

    def distance_callback(self, msg):
        if self.pose is None:
            return

        twist = Twist()

        
        if self.pose.x <= self.min_x:
            self.state = "turning"
            self.turning_direction = 1
        elif self.pose.x >= self.max_x:
            self.state = "turning"
            self.turning_direction = -1
        if self.pose.y <= self.min_y:
            self.state = "turning"
            self.turning_direction = 1
        elif self.pose.y >= self.max_y:
            self.state = "turning"
            self.turning_direction = -1

        
        if self.state == "forward":
            if msg.range < self.min_distance:
                
                self.state = "turning"
                self.turning_direction = 1 if random.random() < 0.5 else -1
                twist.linear.x = 0.0
                twist.angular.z = self.angular_speed * self.turning_direction
                dir_str = "balra" if self.turning_direction == 1 else "jobbra"
                self.get_logger().warn(f'Akadály észlelve ({msg.range:.2f} m) → Fordulás {dir_str}')
            else:
                
                twist.linear.x = self.linear_speed
                twist.angular.z = 0.0
                self.get_logger().info(f'Szabad út ({msg.range:.2f} m) → Előrehaladás')

        elif self.state == "turning":
            if msg.range >= self.min_distance:
                
                self.state = "forward"
                twist.linear.x = self.linear_speed
                twist.angular.z = 0.0
                self.get_logger().info(f'Út megtalálva ({msg.range:.2f} m) → Egyenesen haladás')
            else:
                
                twist.linear.x = 0.0
                twist.angular.z = self.angular_speed * self.turning_direction
                dir_str = "balra" if self.turning_direction == 1 else "jobbra"
                self.get_logger().warn(f'Fordulás {dir_str} az akadály miatt ({msg.range:.2f} m)')

        
        self.pub_cmd.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = ControllerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
