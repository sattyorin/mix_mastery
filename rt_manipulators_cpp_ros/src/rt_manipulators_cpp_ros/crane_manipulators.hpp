#include <optional>
#include <thread>

#include <ros/ros.h>
#include <std_srvs/Float32MultiArray.h>

namespace rt_manipulators_cpp_ros {

class CraneManipulators {
 public:
  CraneManipulators();
  ~CraneManipulators();

 private:
  ros::NodeHandle nh_;
  void writeCurrentCallback(const std_msgs::Float32MultiArray::ConstPtr& msg);
};
}  // namespace rt_manipulators_cpp_ros

