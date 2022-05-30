import rospy
from std_msgs.msg import String
from ros_demo.msg import Jake

class PublisherDemo():
    """A class to implment a simple publisher
    """

    def __init__(self):
        """Class constructor, here we define any data fields etc.
        """

    def init_node(self, ns="~")->None:
        """Init node function, reads any parameters from ROS to setup the node

        Args:
            ns (str, optional): The namespace the node is in. Defaults to "~".
        """

        # read a parameter here, we want the topic to publish to
        topic = rospy.get_param(ns + "topic")
        print("The pub topic is: ", topic)

        # define the publisher object here 
        self.pub = rospy.Publisher(topic,String,queue_size=10)

    def talk(self)->None:
        """Publish some information, use a while loop to keep publishing
        """

        # define the rate at which we run this loop
        rate = rospy.Rate(10)

        # write a loop to publish a message
        while not rospy.is_shutdown():

            # build a message
            msg = String()
            msg.data = "message to the void"

            # publish a message
            self.pub.publish(msg)

            # sleep for some time
            rate.sleep() 




