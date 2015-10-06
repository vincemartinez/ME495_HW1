import rospy
from std_msgs.msg import String


def talker():
	pub = rospy.Publisher('chatter', String, queue_size=10)
	rospy.init_node('fig8')
	rate=rospy.Rate(10)
	while not rospy.is_shutdown():
		#insert stuff here based on "ROS tutorial 3: publishers and subscribers in c++ & python (video on Anis Koubaa's youtube channel)"


def fig8_follow():
#You will likely want to call the turtle1/teleport absolute service to get the turtle located and
#oriented correctly for the t = 0 case.
	rospy.wait_for_service('turtle1/teleport_absolute')
	teleport_absolute=rospy.ServiceProxy('turtle1/teleport_absolute', TeleportAbsolute)


if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass

