#!/usr/bin/env python

import sys
import rospy
from hackathon_23.srv import *
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

def get_command_client(x):
    rospy.wait_for_service('get_command')
    try:
        command = rospy.ServiceProxy('get_command', hackathon_23)
        resp1 = command(x)
        return resp1.machine_command
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e


if __name__ == "__main__":
    com = ""
    while True:    # infinite loop
        n = raw_input("\nChoose number of command\n 0 - Turn On \n 1 - Forward\n 2 - Backward\n 3 - Left\n 4 - Right\n 5 - Autorun\n 6 - Stop\n 7 - Turn Off \n 9 - Exit\n Type the command number here: ")
        if int(n) < 8:
            com = get_command_client(n)
        elif n == "9":
            print "\nExit System\n\nGood Bye!"
            break
        else:
            pass

    # x = sys.argv[1]
    # print "Requesting Command: %s"%(get_command_client(x))
