import rospy
from std_msgs.msg import String

class SubscriberDemo():
    """A class to implement a simple subscriber
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
        # self.sub_topic_name = rospy.get_param(ns + "topic_name")

        # define the subscriber object here
        # This takes the following information
        # 1. Topic
        # 2. message type
        # 3. callback function, the function that runs when we get a message
        # 4. the subscriber queue_size
        self.sub = rospy.Subscriber("topic", String, callback=self.callback, queue_size=10)

    def callback(self,msg:String)->None:
        """The callback function, this function runs everytime we get a message on the topic
        in self.sub

        Args:
            msg (String): the incoming message
        """

        print(msg.data)



