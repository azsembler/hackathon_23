#!/usr/bin/env python

from hackathon_23.srv import *
import rospy

def handle_get_command(req):
    x = req.command
    command = "";
    if x == "0":
        command = "Start"
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
    else:
        pass

    print "Command Recieve -> [%s]"%(command)
    return command

def get_command_server():
    rospy.init_node('get_command_server')
    s = rospy.Service('get_command', hackathon_23, handle_get_command)
    print "Ready to get your command: "
    rospy.spin()


if __name__ == "__main__":
    get_command_server()
