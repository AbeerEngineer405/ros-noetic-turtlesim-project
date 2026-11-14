#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("Received: %s", data.data)

rospy.init_node('smart_subscriber')

rospy.Subscriber('/smart_message', String, callback)

rospy.spin()

