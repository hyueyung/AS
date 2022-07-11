# Description
This package contains a node that forms part of the ROS system controlling a 4WD robot that requires velocity correction on its front left and rear right wheel due to a incorrect wheel size. This node, vel_adjust_node, acts as a temporary fix before the new set of wheels arrives. The node reads the velocity messages for all 4 wheels from the name-space /wheel-vel, calculates the adjusted velocities for the problematic wheels and publishes the adjusted velocities to /front_left_adj and /rear_right_adj.

# How to launch the node
1. Download the vel_adjust folder and place the folder inside the /src folder of your 4WD robot workspace.
2. Make sure the vel_adjust/scripts/vel_adjust_node.py is executable after download. If it is not an executable, run the following bash command in the script folder:
''''
sudo chmod +x vel_adjust_node.py
''''
3. Use the following command to launch the node (from the workspace folder):
''''
roslaunch vel_adjust vel_adjust_node.py
''''

# Dependencies
rospy and std_msgs are the only 2 dependencies of this package.

# My comment
Thank you very much for giving me the opportunity to carry out the assessment. It has taken me about 3 hours up to this point. I would not be able to finish the assessment this quickly (although still an hour longer than the standard time) if I didn't learn ROS1 all over again and reprogramed my remote control car using ROS after the interview.

Once again, it was very nice speaking to you all last week. I had fun learning ROS over the weekend and am excited to be taking this assessment. Thank you very much for your time and consideration and I look forward to hearing from you soon.

Yue Yung
