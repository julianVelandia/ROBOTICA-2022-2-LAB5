import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import termios, sys, os
import math

TERMIOS = termios

class PhantomX:

    def joint_publisher(self, points: [[]], is_degree=None):

        pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
        rospy.init_node('joint_publisher', anonymous=False)
        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
        point = JointTrajectoryPoint()

        for pointArray in points:
            if pointArray[0] == '':
                if menu_while() == 'x':
                    break
                else:
                    continue

            if is_degree is not None:
                pointArray = degrees_to_radians(pointArray)

	
            point.positions = pointArray
            point.time_from_start = rospy.Duration(0.5)
            state.points.append(point)
            pub.publish(state)
            rospy.sleep(1)



def menu_while():
    while True:
        key = input('\nSalto de linea '
                    '\n\n  - Pulse x para finalizar '
                    '\n  -Pulse c para continuar\n')
        if key.lower() == 'x' or key.lower() == 'c':
            break
    return key


def degrees_to_radians(degrees: []):
    return list(map(lambda d: (float(d) * math.pi / 180), degrees))
