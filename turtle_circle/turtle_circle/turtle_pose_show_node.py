# import ros2 python api
import rclpy
from rclpy.node import Node
import math

# import standard message format
from turtlesim.msg import Pose


# define node class
class TurtlePoseSubscriber(Node):
    def __init__(self, node_name: str) -> None:
        super().__init__(node_name)
        # print info
        self.get_logger().info("turtle_pse_show node created!")

        # create a topic subscriber
        # parameters:
            # msg_type: the type of message
            # topic: the name of topic
            # qos_profile: a QoSProfile for setting the communication policy or a history depth to store
        self.subscriber = self.create_subscription(msg_type=Pose, topic="turtle1/pose", callback=self._subscribe, qos_profile=5)

    def _subscribe(self, pose):
        # print info
        radius = pose.linear_velocity / pose.angular_velocity if pose.angular_velocity != 0 else 0

        self.get_logger().info('Turtle is at: x: {0:.2f}, y: {1:.2f}, theta: {2:.2f}, radius: {3:.2f}'.format(pose.x, pose.y, pose.theta, radius))


def main():
    # initialize ros2
    rclpy.init()

    # execute callbacks until shutdown
    rclpy.spin(node=TurtlePoseSubscriber(node_name="turtle_pose_show_node"))

    # shutdown a previously initialization
    rclpy.shutdown()


if __name__ == '__main__':
    main()
