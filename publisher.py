#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

rospy.init_node('smart_publisher')
pub = rospy.Publisher('/smart_message', String, queue_size=10)

rate = rospy.Rate(1)

while not rospy.is_shutdown():
    message = "Smart Methods Robotics"
    rospy.loginfo(message)
    pub.publish(message)
    rate.sleep()

