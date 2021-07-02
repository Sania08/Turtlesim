#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
def pose_callback(pose_message):
    pose_msg.x=pose_message.x
    pose_msg.y=pose_message.y
    pose_msg.theta=pose_message.theta
    pose_msg.linear_velocity=pose_message.linear_velocity
    pose_msg.angular_velocity=pose_message.angular_velocity
    #print(pose_msg)

def dist_cal(x1,y1,x2,y2):
    dist=abs(math.sqrt(((x1-x2)**2)+((y1-y2)**2)))
    return dist

def ang_cal(x1,y1,x2,y2):
    angle_cal=math.atan2(y1-y2,x1-x2)
    return angle_cal

def move():
    rospy.init_node('onemotion_try', anonymous=True)
    velocity_publisher=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    pose_subscriber=rospy.Subscriber('/turtle1/pose',Pose,pose_callback)
    vel_msg=Twist()
    global pose_msg
    pose_msg=Pose()
    goal_x=int(input("enter x direction:"))
    goal_y=int(input("enter y direction"))

    while (True):
        #dist=abs(math.sqrt(((goal_x-pose_msg.x)**2)+((goal_y-pose_msg.y)**2)))
        dist_diff=dist_cal(goal_x,goal_y,pose_msg.x,pose_msg.y)
        #angle=math.atan2(goal_y-pose_msg.y,goal_x-pose_msg.x)
        angle=ang_cal(goal_x,goal_y,pose_msg.x,pose_msg.y)
        vel_msg.linear.x= 0.5 * (dist_diff)
        vel_msg.linear.y = 0
        vel_msg.linear.z= 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 3 * (angle-pose_msg.theta)
        velocity_publisher.publish(vel_msg)
        print(pose_msg)
        #loop_rate.sleep()
        if (dist_diff<0.01):
            #vel_msg.linear.x=0
            #vel_msg.angular.z=0
            #velocity_publisher.publish(vel_msg)
            #print(pose_msg)
            break

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException: pass
