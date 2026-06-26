
# Conclusion

This lab provided practical experience in implementing reactive navigation for a mobile robot using LiDAR sensor data in a ROS 2 and Gazebo simulation environment. By subscribing to the `/scan` topic and processing `LaserScan` messages, we were able to extract directional distance information for the front, left, and right regions around the TurtleBot3 and use that data to drive real-time motion decisions through the `/cmd_vel` topic.

The key learning outcomes achieved include interpreting raw LiDAR range arrays, handling invalid sensor values such as `inf` and `NaN`, dividing the scan into meaningful directional regions, and implementing a threshold-based reactive control loop for obstacle detection and avoidance. The experience also reinforced the ROS 2 node structure — publishers, subscribers, and callbacks — in a practical, sensor-driven context.

The main challenges encountered involved tuning the distance thresholds appropriately for the simulated environment. A threshold set too high caused the robot to stop prematurely in open space, while one set too low resulted in near-collision behaviour. Oscillation during turning was also observed when the robot repeatedly detected obstacles at similar distances on both sides, highlighting the need for hysteresis or a more robust decision-making strategy. Additionally, ensuring stable distance readings required averaging or minimum filtering over scan regions rather than relying on single range values, which can be noisy.

Overall, this lab established a foundational understanding of how raw sensor data can be translated into reliable control decisions without any map or pre-planned path, forming the basis for more advanced navigation techniques such as potential fields, path planning, and sensor fusion.
