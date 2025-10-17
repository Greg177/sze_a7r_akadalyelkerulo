import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range
import math

class SimSensor(Node):
    def __init__(self):
        super().__init__('sim_sensor')
        self.pub = self.create_publisher(Range, 'distance', 10)
        self.angle = 0.0
        self.create_timer(0.1, self.timer_callback)

    def timer_callback(self):
        msg = Range()
        
        msg.range = 0.5 + 0.5 * math.sin(self.angle)
        self.angle += 0.1
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = SimSensor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
