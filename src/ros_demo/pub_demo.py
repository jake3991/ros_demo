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
        # self.sub_topic_name = rospy.get_param(ns + "topic_name")

        # define the publisher object here
        # This takes the following information
        # 1. Topic
        # 2. message type
        # 3. callback function, the function that runs when we get a message
        # 4. the subscriber queue_size
        self.pub = rospy.Publisher("topic", String, queue_size=10)

    def talk(self)->None:
        """Publish some information, use a while loop to keep publishing
        """

        # define the rate at which we run this loop
        # the rate is in hz
        rate = rospy.Rate(10) 

        # while ros has not shutdown, loop
        while not rospy.is_shutdown():

            # package up a nice string with a time stamp so we can tell the messages apart
            hello_str = "hello world %s" % rospy.get_time()

            # publish the message
            self.pub.publish(hello_str)

            # sleep as per the rate set above, enforcing the rosrate
            rate.sleep()




