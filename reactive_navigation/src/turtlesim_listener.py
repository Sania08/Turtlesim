#!/usr/bin/env python
import rospy
import tf
import math
from geometry_msgs.msg import Twist
import turtlesim.srv
import roslib

def dist_cal(x1,y1,x2,y2):
    dist=abs(math.sqrt(((x1-x2)**2)+((y1-y2)**2)))
    return dist

def ang_cal(x1,y1,x2,y2):
    angle_cal=math.atan2(y1-y2,x1-x2)
    return angle_cal

def move(translation,rotation):
    global follower_vel_pub
    x_follower_frame1=translation[0]
    y_follower_frame1=translation[1]
    follower_vel=Twist()
    follower_vel.linear.x= 0.5 * (dist_cal(x_follower_frame1,y_follower_frame1,0,0))
    follower_vel.linear.y = 0
    follower_vel.linear.z= 0
    follower_vel.angular.x = 0
    follower_vel.angular.y = 0
    follower_vel.angular.z = 4 * (ang_cal(x_follower_frame1,y_follower_frame1,0,0))
    follower_vel_pub.publish(follower_vel)
    rate.sleep()

if __name__=='__main__':
    global follower_vel_pub
    #Initializing the listener node
    rospy.init_node('turtle_transform_listener')
    tf_listener=tf.TransformListener()

    #Use service to spawn the second turtle
    rospy.wait_for_service('spawn')
    spawner=rospy.ServiceProxy('spawn',turtlesim.srv.Spawn)
    spawner(4,2,0,'turtle2')
    follower_vel_pub=rospy.Publisher('turtle2/cmd_vel',Twist,queue_size=1)
    rate=rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            (trans,rot)=tf_listener.lookupTransform('/turtle2_frame','/turtle1_frame',rospy.Time(0))
        except(tf.LookupException,tf.ConnectivityException,tf.ExtrapolationException):
            continue
        move(trans,rot)

        