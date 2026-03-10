import rclpy
from rclpy.node import Node
import os

class SimpleNode(Node):
    def __init__(self):
        super().__init__('simple_node')
        # Task 3: Declare parameter
        self.declare_parameter('student_name', 'student_name not set')
        name = self.get_parameter('student_name').get_parameter_value().string_value

        # Task 1: Custom Log Message
        self.get_logger().info('Welcome to Mobile Robotics Lab')

        # Task 2: Counter logic
        count_file = os.path.join(os.getcwd(), 'counter.txt')
        count = 0
        if os.path.exists(count_file):
            with open(count_file, 'r') as f:
                count = int(f.read().strip())
        count += 1
        with open(count_file, 'w') as f:
            f.write(str(count))

        self.get_logger().info(f'Run count: {count}')
        self.get_logger().info(f'Student Name: {name}')

def main(args=None):
    rclpy.init(args=args)
    node = SimpleNode()
    rclpy.spin_once(node, timeout_sec=0.1)
    node.destroy_node()
    rclpy.shutdown()