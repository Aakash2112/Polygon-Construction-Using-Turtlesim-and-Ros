#!/usr/bin/env python

import rospy
from turtle_polygon.srv import Polygon, PolygonRequest

def polygon_client():
    # Wait for the /polygon service to become available
    rospy.wait_for_service('/polygon')

    # Create a proxy for the /polygon service
    polygon = rospy.ServiceProxy('/polygon', Polygon)

    # Get the number of sides from the user
    sides = input("Enter the number of sides: ")

    # Call the /polygon service with the number of sides
    req = PolygonRequest(sides)
    res = polygon(req)

    if res.success:
        rospy.loginfo("Polygon drawn successfully!")
    else:
        rospy.logwarn("Failed to draw polygon.")
    
if __name__ == '__main__':
    rospy.init_node('polygon_client')
    polygon_client()
