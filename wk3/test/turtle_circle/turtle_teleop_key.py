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
        # Moving in a circle, V = R * omega
        msg.linear.x = 2.0  # Linear velocity
        msg.angular.z = 1.0  # Angular velocity, calculated as w = V/R (here R = 2)

        global theta

        R = 2.0
        cX = 0.0
        cY = 1.0
        
        msg_text = "X: {}, Y: {}, theta: {}".format(cX + R * math.sin(theta + 0.5 * 1.0), cY + R * math.cos(theta + 0.5 * 1.0), theta)
        theta = theta + 0.5 * 1.0
        
        self.publisher.publish(msg)
        self.get_logger().info(msg_text)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()