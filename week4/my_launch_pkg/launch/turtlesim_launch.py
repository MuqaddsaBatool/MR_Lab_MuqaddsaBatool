from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',        # which package
            executable='turtlesim_node', # which node
            name='sim',                  # name in ROS2 graph
            output='screen'              # print logs to terminal
        ),
        Node(
            package='turtlesim',
            executable='turtle_teleop_key',
            name='teleop',
            output='screen'
        )
    ])
