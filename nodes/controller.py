#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

# youBotOn = False
# coordinateInitialized = False
# startX=0.0
# startY=0.0

# def stopYouBot():
#     twist = Twist()
#
#     twist.linear.x = 0
#     twist.linear.y = 0
#     twist.angular.z = 0
#
#     youBot_publisher.publish(twist)
#
# # Moves youBot based on command in /input topic
# def move_callback(message):
#     command = message.data.lower()
#     twist = Twist()
#
#     rospy.loginfo("Swith is %s" %("ON" if youBotOn else "OFF"))
#
#     if  command == "forward":
#         rospy.loginfo("Moving forward ...")
#         twist.linear.x = rospy.get_param("/x_vel", 0.2)
#         twist.linear.y = 0
#
#     elif command == "backward":
#         rospy.loginfo("Moving backward ...")
#         twist.linear.x = rospy.get_param("/x_vel", 0.2) * -1.0
#         twist.linear.y = 0
#
#     elif command == "left":
#         rospy.loginfo("Moving left ...")
#         twist.linear.x = 0
#         twist.linear.y = rospy.get_param("/y_vel",0.2)
#         twist.angular.z = rospy.get_param("/theta_val", 0)
#
#     elif command == "right":
#         rospy.loginfo("Moving right ...")
#         twist.linear.x = 0
#         twist.linear.y = rospy.get_param("/y_vel",0.2) * -1.0
#         twist.angular.z = rospy.get_param("/theta_val", 0)
#
#     if youBotOn:
#         youBot_publisher.publish(twist)
#     else:
#         rospy.loginfo("youBot is off")
#
# #Set flag based on command in /event_in topic
# def trigger_callback(message):
#     global youBotOn
#     command = message.data.lower()
#
#     if command == "e_start":
#         rospy.loginfo("Turning on ...")
#         youBotOn = True
#
#     elif command == "e_stop":
#         rospy.loginfo("Turning off ...")
#         youBotOn = False
#
#         stopYouBot()

# Checks distance for start while moving and stops when
# the distance is equal to distance in parameter
# def odom_callback(message):
#     global coordinateInitialized
#     global startX
#     global startY
#
#     if(not coordinateInitialized):
#         coordinateInitialized = True
#
#         startX = message.pose.pose.position.x
#         startY = message.pose.pose.position.y
#
#     currentX = message.pose.pose.position.x
#     currentY = message.pose.pose.position.y
#
#     distance = (((currentX - startX) ** 2) + ((currentY - startY) ** 2)) ** 0.5
#
#     targetDistance = rospy.get_param("/distance", 0.5)
#
#     if(distance >= targetDistance):
#         startX = currentX
#         startY = currentY
#
#         rospy.loginfo("Current position, X: %s, Y: %s" %(startX, startY))
#         stopYouBot()


def main():
    global youBot_publisher

    rospy.init_node('controller')



    # Subscribing to navigation commands
    # rospy.Subscriber('/input', String, move_callback)

    # Subscribing to start/stop commands
    # rospy.Subscriber('/event_in', String, trigger_callback)

    # Subscribing to get Odometry data for current X,Y coordinates
    # rospy.Subscriber("/odom", Odometry, odom_callback)

    # Publisher for youBot to navigate
    # youBot_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    #
    # rate = rospy.Rate(10)
    # while not rospy.is_shutdown():
    #     rate.sleep()
    # pass

if __name__ == '__main__':
    main()
