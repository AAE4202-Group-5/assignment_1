import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

import math


theta = 270 / 180 * math.pi

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_control_node')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.publish_command)  # 2 Hz
        self.get_logger().info("Turtle Control Node has started.")

    def publish_command(self):
        msg = Twist()
        # V = R * w, w = V/R (R = 2)
        msg.linear.x = 2.0  
        msg.angular.z = 1.0  
        
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()