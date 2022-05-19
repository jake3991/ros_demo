#pragma once
#include "ros/ros.h"
#include "std_msgs/String.h"

//class definition for  the pub_demo class
class pub_demo
{
    private:
        /* data */
        ros::NodeHandle n;
        ros::Publisher pub;
    public:
        pub_demo(); //class con
        ~pub_demo(); //class des
        void init_node(); //create the publisher object
        void talker(); //while loop, published message at some ros rate
        void jakes_question(int flag);
};


