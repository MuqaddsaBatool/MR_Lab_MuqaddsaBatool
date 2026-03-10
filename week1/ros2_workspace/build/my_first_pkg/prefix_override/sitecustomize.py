import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/Muqaddsa/ros2_workspace/install/my_first_pkg'
