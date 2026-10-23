#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

import numpy as np
from sensor_msgs.msg import LaserScan
from ackermann_msgs.msg import AckermannDriveStamped

class GapFollowNode(Node):
    """ 
    Implement Gap Following on the car
    This is just a template, you are free to implement your own node!
    """
    def __init__(self):
        super().__init__('gap_follow_node')
        #TODO: Topics & Subs, Pubs
        lidarscan_topic = ...
        drive_topic = ...

        #TODO: Subscribe to LIDAR
 
        #TODO: Publish to drive


        self.angle = 0.0
        self.ranges = []

    def preprocess_lidar(self, ranges, angle_min, angle_increment):
        """TODO: Preprocess the LiDAR scan array. Expert implementation includes:
            1. Setting each value to the mean over some window
            2. Rejecting high values (eg. > 3m)
        """
        proc_ranges = np.array(ranges)
        min_angle = np.radians(-70)
        max_angle = np.radians(70)
        
        self.min_indx = min_indx
        self.max_indx = max_indx
        return proc_ranges, min_indx, max_indx

    def find_max_gap(self, free_space_ranges):
        """TODO: Return the start index & end index of the max gap in free_space_ranges """
        min_indx = self.min_indx
        max_indx = self.max_indx

        start = min_indx
        end = min_indx
        current_start = min_indx - 1
        longest_duration = 0

        
        self.proc_ranges = free_space_ranges
        return start, end
    
    def find_best_point(self, start_i, end_i, ranges, angle_min, angle_increment):
        """TODO: Start_i & end_i are start and end indices of max-gap range, respectively
        Return index of best point in ranges
        Naive: Choose the furthest point within ranges and go there
        """
        

        return self.angle

    def lidar_callback(self, data):
        """ Process each LiDAR scan as per the Follow Gap algorithm & publish an AckermannDriveStamped Message """
        ranges = data.ranges
        angle_min = data.angle_min
        angle_increment = data.angle_increment
        proc_ranges, min_indx, max_indx = self.preprocess_lidar(ranges, angle_min, angle_increment)
        
        #TODO: Find closest point to LiDAR
        

        #TODO: Dynamic safety bubble size based on speed
        

        #TODO: Eliminate all points inside 'bubble' (set them to zero)
        

        #TODO: Find max length gap
        

        #TODO: Find the best point in the gap
        

        #TODO: Increase speed if the best angle is close to zero (straight ahead)
       

        #TODO: Smooth the steering angles to avoid abrupt changes


        #TODO: Publish Drive message
        

def main(args=None):
    rclpy.init(args=args)
    print("GapFollow Initialized")
    gap_follow_node = GapFollowNode()
    rclpy.spin(gap_follow_node)

    gap_follow_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
