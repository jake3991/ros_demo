#pragma once
#include "ros/ros.h"
#include "std_msgs/String.h"

//class definition for  the pub_demo class
class sub_demo
{
    private:
        /* data */
        ros::NodeHandle n;
        ros::Subscriber sub;
    public:
        sub_demo();
        ~sub_demo();
        void init_node();
        void callback(const std_msgs::String::ConstPtr& msg);
};


