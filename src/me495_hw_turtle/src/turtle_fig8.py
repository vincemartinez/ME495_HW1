#!/usr/bin/env python
#shebang!

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute
import math
from math import cos, pi, sin, sqrt
import dynamic_reconfigure



def fig8_follow():
	
	#Create publisher, initialize node, set rate, create a Twist
	pub_twist = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
	rospy.init_node('fig8')
	rate=rospy.Rate(100)
	vel_msg=Twist()

	#Set initial position using turtlesim's TeleportAbsolute service
	rospy.wait_for_service('turtle1/teleport_absolute')
	teleport_absolute=rospy.ServiceProxy('turtle1/teleport_absolute', TeleportAbsolute)
	initial_position=teleport_absolute(6.75,6.25,.464) # x & y chosen to re-center trajectory, .464 radians based on initial angle of magnitude of velocity

	#Set period and get initial time
	T=rospy.get_param('~T')
	#T=4
	t_init=rospy.get_time()

	#begin trajectory following loop
	while not rospy.is_shutdown():


		t_curr=rospy.get_time()-t_init

		x_vel=12*pi*cos(4*pi*t_curr/T)/T                #Derivative of provided x(t)
		y_vel=6*pi*cos(2*pi*t_curr/T)/T                 #Derivative of provided y(t)
		x_acc=(-48*pi**2*sin(4*pi*t_curr/T))/T**2       #Derivative of x_vel
		y_acc=(-12*pi**2*sin(2*pi*t_curr/T))/T**2       #Derivative of y_vel

		vel_msg.linear.x= sqrt(x_vel**2+y_vel**2)        #Magnitude of derivatives of provided x(t) & y(t)
		vel_msg.linear.y=0
		vel_msg.linear.z=0 #These values are not used in kinematic-car model

		vel_msg.angular.x=0
		vel_msg.angular.y=0
		vel_msg.angular.z=((y_acc*x_vel)-(x_acc*y_vel))/((x_vel**2)+(y_vel**2)) #solution to system

		pub_twist.publish(vel_msg)

		rate.sleep()





if __name__ == '__main__':
	try:
		fig8_follow()
	except rospy.ROSInterruptException:
		pass

