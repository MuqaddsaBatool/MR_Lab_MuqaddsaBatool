import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class DrawCircle(Node):
    def __init__(self):
        super().__init__('draw_circle')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.move_turtle)

    def move_turtle(self):
        msg = Twist()

        # Set velocities
        msg.linear.x = 2.0      # forward speed
        msg.angular.z = 1.0     # rotation speed

        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = DrawCircle()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()