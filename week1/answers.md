Lab 1 Answers

1. Definitions

Node: A single-purpose executable in ROS 2 that communicates with other nodes.

Topic: A named bus over which nodes exchange messages using a publish/subscribe model.

Package: A container for ROS 2 code, data, and configuration files, making software easy to share and build.

Workspace: A directory containing ROS 2 packages that you are currently developing or using.

2. Sourcing

Sourcing is required to set up environment variables (like PATH and PYTHONPATH) so the shell knows where ROS 2 commands and your custom packages are located. Without sourcing, commands like ros2 run will result in "command not found".

3. colcon build

colcon build compiles the source code in your workspace. It generates four folders: build (intermediate files), install (executables and setup scripts), log (build logs), and sometimes test_results.

4. entry_points

The console_scripts inside setup.py maps a terminal command (e.g., simple_node) to a specific Python function (e.g., main in simple_node.py), allowing ROS 2 to execute the script.

