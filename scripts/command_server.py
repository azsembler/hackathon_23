#!/usr/bin/env python

from get_command.srv import *
import rospy

def handle_get_command(req):
    print "Returning [%s]"%(req)
    return GetCommandResponse(req)

def get_command_server():
    rospy.init_node('get_command_server')
    s = rospy.Service('get_command_server', Empty, handle_get_command)
    print "Ready to get your command: "
    rospy.spin()


if __name__ == "__main__":
    get_command_server()
