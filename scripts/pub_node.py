#!/usr/bin/env python

import rospy
from ros_demo.pub_demo import PublisherDemo


if __name__ == "__main__":

    # use rospy to setup this script as a node
    rospy.init_node("talker", log_level=rospy.INFO)

    # instaciate the node, in this case our SubsciberDemo
    node = PublisherDemo()

    # call init node to setup the node
    node.init_node()

    # print statement to indicate what is happening
    rospy.loginfo("I'm talking!!!")

    # print statement to indicate what is happening
    node.talk()
