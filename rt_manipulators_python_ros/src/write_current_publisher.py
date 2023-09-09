#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32MultiArray
import numpy as np


class CraneManipulators:
    def __init__(self) -> None:
        rospy.init_node("crane_manipulators_python", anonymous=True)
        self.publisher = rospy.Publisher(
            "servo_current", Float32MultiArray, queue_size=10
        )

    def write_current(self, current_array: np.ndarray):
        self.publisher(current_array)
