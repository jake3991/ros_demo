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
        pub_demo();
        ~pub_demo();
        void init_node();
        void talker();
};


