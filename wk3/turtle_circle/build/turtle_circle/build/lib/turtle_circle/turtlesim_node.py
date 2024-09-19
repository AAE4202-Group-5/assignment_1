import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class TurtlePoseShow(Node):
    def __init__(self):
        super().__init__('turtle_pose_show_node')
        self.subscription = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.get_logger().info("Turtle Pose Show Node has started.")

    def pose_callback(self, msg):
        self.get_logger().info(f"Pose: x={msg.x:.2f}, y={msg.y:.2f}, theta={msg.theta:.2f} | Circle radius: 2")

def main(args=None):
    rclpy.init(args=args)
    node = TurtlePoseShow()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()