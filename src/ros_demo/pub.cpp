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
    this->pub = this->n.advertise<std_msgs::String>("white_board",10);
}

/**
 * @brief the function that will send some data out to our topic
 *  
 */
void pub_demo::talker(){

    //define the ros rate
    ros::Rate loop_rate(10);

    //counter varible for messages
    int count = 0;

    while(ros::ok()){

        //instance of a message
        std_msgs::String msg;

        //populate that message
        std::stringstream ss;
        ss << "hello world" << count;
        msg.data = ss.str();

        //publish the message
        this->pub.publish(msg);

        //sleep per the loop
        loop_rate.sleep();
        count += 1;

    }
  
}

void pub_demo::jakes_question(int flag){


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