import rospy
from std_msgs.msg import String

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

        # define the publisher object here

    def talk(self)->None:
        """Publish some information, use a while loop to keep publishing
        """

        # define the rate at which we run this loop
        
        # write a loop to publish a message




