#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import time

rospy.init_node('draw_square')
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
time.sleep(1)

move = Twist()

for i in range(4):
    # Move forward
    move.linear.x = 2.0
    move.angular.z = 0.0
    pub.publish(move)
    time.sleep(2)

    # Stop
    move.linear.x = 0.0
    pub.publish(move)
    time.sleep(0.5)

    # Turn 90 degrees
    move.angular.z = 1.57
    pub.publish(move)
    time.sleep(1)

    # Stop turning
    move.angular.z = 0.0
    pub.publish(move)
    time.sleep(0.5)

move.linear.x = 0.0
move.angular.z = 0.0
pub.publish(move)
