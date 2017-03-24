#!/usr/bin/env python

import rospy
from hackathon_23.srv import *
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

youBotOn = False
coordinateInitialized = False
startX=0.0
startY=0.0

def execute_command(com):
    command = com
    global youBotOn
    global coordinateInitialized
    global startX
    global startY
    twist = Twist()
    lin_x = 0.0
    lin_y = 0.0
    ang_z = 0.0

    if  command == "Forward":
        rospy.loginfo("Moving forward ...")
        lin_x = rospy.get_param("/x_vel", 0.2)
        lin_y = 0.0

    elif command == "Backward":
        rospy.loginfo("Moving backward ...")
        lin_x = rospy.get_param("/x_vel", 0.2) * -1.0
        lin_y = 0

    elif command == "Left":
        rospy.loginfo("Moving left ...")
        lin_x = 0
        lin_y = rospy.get_param("/y_vel",0.2)
        ang_z = rospy.get_param("/theta_val", 0)

    elif command == "Right":
        rospy.loginfo("Moving right ...")
        lin_x = 0
        lin_y = rospy.get_param("/y_vel",0.2) * -1.0
        ang_z = rospy.get_param("/theta_val", 0)

    elif command == "Stop":
        rospy.loginfo("Moving backward ...")
        lin_x = 0
        lin_y = 0
        ang_z = 0

    elif command == "On":
        rospy.loginfo("Turning on ...")
        youBotOn = True

    elif command == "Off":
        rospy.loginfo("Turning off ...")


    if youBotOn:
        twist.linear.x = lin_x
        twist.linear.y = lin_y
        twist.angular.z = ang_z
        youBot_publisher.publish(twist)
        if command =="Off":
            youBotOn = False
    else:
        rospy.loginfo("youBot is off")

    # rospy.loginfo("Swith is %s" %("ON" if youBotOn else "OFF"))

def handle_get_command(req):

    x = req.command
    command = "";
    if x == "0":
        command = "On"
    elif x== "1":
        command = "Forward"
    elif x== "2":
        command = "Backward"
    elif x== "3":
        command = "Left"
    elif x== "4":
        command = "Right"
    elif x== "5":
        command = "Autorun"
    elif x== "6":
        command = "Stop"
    elif x== "7":
        command = "Off"
    else:
        pass

    print "Command Recieve -> [%s]"%(command)
    # return command
    execute_command(command)
    return command

# def usage():
#     return "%s [x]"%sys.argv[0]

def get_command_server():
    rospy.init_node('get_command_server')
    s = rospy.Service('get_command', hackathon_23, handle_get_command)
    print "Ready to get your command: "
    rospy.spin()


if __name__ == "__main__":
    global youBot_publisher
    youBot_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    get_command_server()
