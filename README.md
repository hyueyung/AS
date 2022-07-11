# Description
This package contains a node that forms part of the ROS system controlling a 4WD robot that requires velocity correction on its front left and rear right wheel due to a certain mechanical error. This node, vel_adjust_node, acts as a temporary fix before the new set of wheels arrive. It reads the velocity messages for all 4 wheels from the name-space /wheel-vel and also calculated the adjusted velocities for the problematic wheels.

# How to launch the node
1. Download the vel_adjust folder and place the folder inside the /src folder of your 4WD robot workspace.
To launch the node (from the workspace folder):
''''
roslaunch vel_adjust vel_adjust_node.py
''''

# Dependencies
rospy and std_msgs are the only 2 dependencies of this package.




# Comment
Thank you very much again for the It took my about 2.5 hours up to this point

It was very nice speaking to you all last week. I had fun learning ROS over the weekend and had some fun taking this assessment. Thank you very much for your time and consideration again and I look forward to hearing from you again.

Yue
