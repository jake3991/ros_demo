#include "ros_demo/pub_demo.h"

/**
 * @brief Construct a new pub demo::pub demo object
 * 
 */
pub_demo::pub_demo(){}

/**
 * @brief Destroy the pub demo::pub demo object
 * 
 */
pub_demo::~pub_demo(){}

/**
 * @brief The same init node function we wrote in python, define out subscriber object
 * 
 */
void pub_demo::init_node(){

    //define the publisher object
}

/**
 * @brief the function that will send some data out to our topic
 *  
 */
void pub_demo::talker(){

    //define the ros rate

    //counter varible for messages
    int count = 0;

    //while loop, run while ros is active to publish some data
  
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

    ros::init(argc, argv, "talker_cpp");
    pub_demo node = pub_demo();
    node.init_node();
    node.talker();

}