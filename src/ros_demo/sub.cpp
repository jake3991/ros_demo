#include "ros_demo/sub_demo.h"
#include "std_msgs/String.h"

/**
 * @brief Construct a new pub demo::pub demo object
 * 
 */
sub_demo::sub_demo(){}

/**
 * @brief Destroy the pub demo::pub demo object
 * 
 */
sub_demo::~sub_demo(){}

/**
 * @brief The same init node function we wrote in python, define out subscriber object
 * 
 */
void sub_demo::init_node(){

    //define some subscriber
    this->sub = this->n.subscribe("white_board",10, &sub_demo::callback,this);
}

/**
 * @brief the function that will run when we get data on our topic
 *  
 */
void sub_demo::callback(const std_msgs::String::ConstPtr& msg){

    //do somthing with this message
    ROS_INFO(msg->data.c_str());
}


/**
 * @brief The main function for this cpp file
 * 
 * @param argc 
 * @param argv 
 * @return int 
 */
int main(int argc, char **argv)
{

    ros::init(argc, argv, "listener_cpp");
    sub_demo node = sub_demo();
    node.init_node();
    ros::spin();

    return 0;

}