#!/usr/bin/env python
import roslib 
import rospy
import tf
import turtlesim.msg
from turtlesim.msg import Pose

def callback_func(pose_msg,turtle_name):
    #Create a transform broadcaster object
    tf_broadcaster=tf.TransformBroadcaster()
    #Euler angles to Quaternion conversion
    rot_quaternion=tf.transformations.quaternion_from_euler(0,0,pose_msg.theta)
    #Translation vector
    trans_vector=(pose_msg.x,pose_msg.y,0)
    current_time=rospy.Time.now()

    tf_broadcaster.sendTransform(trans_vector,rot_quaternion,current_time,turtle_name+"_frame","world")

if __name__=='__main__':
    #Initializing the broadcaster node
    rospy.init_node('turtle_transform_broadcast')
    name=rospy.get_param('~turtle')
    rospy.Subscriber('/%s/pose' % name,Pose,callback_func,name)
    rospy.spin()