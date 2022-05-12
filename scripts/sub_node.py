#!/usr/bin/env python

import rospy
from ros_demo.sub_demo import SubscriberDemo


if __name__ == "__main__":

    # use rospy to setup this script as a node
    rospy.init_node("listener", log_level=rospy.INFO)

    # instaciate the node, in this case our SubsciberDemo
    node = SubscriberDemo()

    # call init node to setup the node
    node.init_node()

    # print statement to indicate what is happening
    rospy.loginfo("I'm listening!!!")

    # block until we recive the ros shutdown signal
    rospy.spin()
