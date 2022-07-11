#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

# Set the adjustment constants for front left and rear right wheel
ACTUAL_FL = 0.87
ACTUAL_RR = 1.35


# Define the publisher nodes that output the adjusted velocities
pub_vel_fl = rospy.Publisher("/wheel_vel/front_left_adj", Float64, 
	queue_size=10)
pub_vel_rr = rospy.Publisher("/wheel_vel/rear_right_adj", Float64, 
	queue_size=10)



def callback_fl(data):
    """
    Callback function for front left
    Publish the adjusted velocity
    """
    print("Velocity (Front-Left): %.4f" % data.data)
    # Calculate the new velocity front_left_adj and publish to the topic
    pub_vel_fl.publish(data.data/ACTUAL_FL)



def callback_fr(data):
    """
    Callback function for front right
    """
    print("Velocity (Front-Right): %.4f" % data.data)
    


def callback_rl(data):
    """
    Callback function for rear left
    """
    print("Velocity (Rear-Left): %.4f" % data.data)
	


def callback_rr(data):
    """
    Callback function for rear right
    Publish the adjusted velocity
    """
    print("Velocity (Rear_Right): %.4f" % data.data)
    # Calculate the new velocity rear_right_adj and publish to the topic
    pub_vel_rr.publish(data.data/ACTUAL_RR)


def vel_adjust():
    # Initialise node and subscribe to the topics in /wheel_vel
    rospy.init_node("vel_adjust_node", anonymous = True)
    rospy.Subscriber("/wheel_vel/front_left", Float64, callback_fl)
    rospy.Subscriber("/wheel_vel/front_right", Float64, callback_fr)
    rospy.Subscriber("/wheel_vel/rear_left", Float64, callback_rl)
    rospy.Subscriber("/wheel_vel/rear_right", Float64, callback_rr)
    
    # Keep running until the node is stopped
    rospy.spin()


if __name__ == '__main__':
    try:
        # vel_adjust is the main function of this node.
        # it reads the velocity messages for all wheels (in no particular
        # order or frequency) for the 4WD robot. It also calculate and output
        # the adjusted velocity values for the front left and rear right
        # wheel.
        vel_adjust()
    except rospy.ROSInterruptException:
        pass
