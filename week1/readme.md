MCT-454L Mobile Robotics - Lab Repository

Student Name: Muqaddsa Batool

Session: Week 1 - ROS 2 Onboarding & First Node

Overview

This repository contains the deliverables for the Mobile Robotics Lab. Week 1 focused on setting up the ROS 2 Humble environment on WSL (Windows Subsystem for Linux), creating a development workspace, and building a Python-based ROS 2 package from scratch.

Repository Structure

week1/

my_first_pkg/: The ROS 2 Python package.

screenshots/: Visual evidence of build and execution.

answers.md: Technical post-lab questions.

Tasks Completed

Workspace Setup: Created ros2_workspace and configured the environment.

Package Creation: Developed my_first_pkg using ament_python.

Node Development: Created simple_node.py with the following features:

Custom log message: "Welcome to Mobile Robotics Lab".

Run persistence: Implemented a file-based counter to track executions.

ROS Parameters: Integrated student_name parameter handling.

💻 Commands Used

# Sourcing ROS 2
source /opt/ros/humble/setup.bash

# Building Workspace
cd ~/ros2_workspace
colcon build

# Sourcing Workspace
source install/setup.bash

# Running the Node with Parameters
ros2 run my_first_pkg simple_node --ros-args -p student_name:="Muqaddsa Batool"


🧠 Reflection

Setting up ROS 2 on WSL provided a great introduction to the Linux-based robotics ecosystem. The most important lesson was understanding the "Source-Build-Source" cycle; forgetting to source the install folder after a build is a common pitfall. Implementing the counter task taught me how ROS nodes interact with the local file system, and using parameters showed how we can dynamically configure a robot's behavior without changing the source code. The environment setup was smooth, and I am now ready for more complex node-to-node communication in future labs.

Note: This repository is part of the MCT-454L course requirements.
