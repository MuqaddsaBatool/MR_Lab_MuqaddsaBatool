import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TriangleMover(Node):

    def __init__(self):
        super().__init__('triangle_mover')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        
        # State machine variables
        self.state = 'forward'       # current state
        self.tick = 0                # counts timer callback
        
        # Tuning values
        self.forward_ticks = 20      # how long to move straight
        self.turn_ticks = 15         # how long to turn

    def timer_callback(self):
        msg = Twist()
        self.tick += 1

        if self.state == 'forward':
            msg.linear.x = 2.0
            msg.angular.z = 0.0
            if self.tick >= self.forward_ticks:
                self.tick = 0
                self.state = 'turn'  # switch state

        elif self.state == 'turn':
            msg.linear.x = 0.0
            msg.angular.z = 2.0      # turning
            if self.tick >= self.turn_ticks:
                self.tick = 0
                self.state = 'forward'  # switch back

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TriangleMover()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()