import rospy
from std_msgs.msg import String

from ros_demo.msg import Jake

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
        topic = rospy.get_param(ns + "topic")
        print("The sub topic is: ", topic)

        # define the subscriber object here
        self.sub = rospy.Subscriber(topic,Jake,callback=self.callback,queue_size=10)

    def callback(self,msg:String)->None:
        """The callback function, this function runs everytime we get a message on the topic
        in self.sub

        Args:
            msg (String): the incoming message
        """

        # do somthing with this message
        print(msg.data)



