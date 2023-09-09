#include <ros/ros.h>
#include <std_srvs/Float32MultiArray.h>

/* https://github.com/rt-net/rt_manipulators_cpp/blob/main/samples/samples01/src/x7_write_current.cpp
    を参考に、トピックで電流制御ができるようにする。
*/

#include <chrono>
#include <cmath>
#include <iostream>
#include <thread>
#include <vector>
#include "rt_manipulators_cpp/hardware.hpp"

namespace rt_manipulators_cpp_ros {

CraneManipulators::CraneManipulators():
  nh_("~"){

  std::string port_name = "/dev/ttyUSB0";
  int baudrate = 3000000;  // 3Mbps
  std::string config_file = "../config/crane-x7_current.yaml";

  ros::Subscriber sub = n.subscribe("write_current", 1000, writeCurrentCallback);

  ROS_INFO("initialized CraneManipulators");
}

CraneManipulators::~CraneManipulators() {}

void CraneManipulators::writeCurrentCallback(const std_msgs::Float32MultiArray::ConstPtr& msg)
{
  std::vector<double>goal_currents = /*need cast?*/ msg->data;
  hardware.set_currents("wrist", goal_currents);
}

} // namespace rt_manipulators_cpp_ros

