#!/usr/bin/env python - to run:rosrun turtlesim turtlesim_node

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from math import radians

def handle_polygon(req):
    # Get the number of sides from the client request
    sides = req.sides

    # Initialize the publisher to control the turtle's movement
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # Initialize the subscriber to get the turtle's current pose
    rospy.Subscriber('/turtle1/pose', Pose, pose_callback)

    # Wait for the pose subscriber to get the first message
    rospy.wait_for_message('/turtle1/pose', Pose)

    # Calculate the angle between sides of the polygon
    angle = radians(360.0 / sides)

    # Move the turtle forward and turn for each side of the polygon
    for i in range(sides):
        move_cmd = Twist()
        move_cmd.linear.x = 1.0
        move_cmd.angular.z = angle
        pub.publish(move_cmd)
        rospy.sleep(1.0)

    return True

def pose_callback(msg):
    rospy.loginfo("Turtle position: x=%0.2f, y=%0.2f", msg.x, msg.y)

def polygon_server():
    rospy.init_node('polygon_server')
    rospy.Service('/polygon', Polygon, handle_polygon)
    rospy.loginfo("Ready to draw polygons!")
    rospy.spin()

if __name__ == '__main__':
    polygon_server()
