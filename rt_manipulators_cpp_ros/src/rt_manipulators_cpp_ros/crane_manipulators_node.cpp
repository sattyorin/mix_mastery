#include <ros/ros.h>

#include "crane_manipulators.hpp"

int main(int argc, char** argv) {
  ros::init(argc, argv, "");
  rt_manipulators_cpp_ros::CraneManipulators crane_manipulators;
  ros::waitForShutdown();
  return EXIT_SUCCESS;
}

