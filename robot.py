import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import termios, sys, os
import math
import time
from get_points import read_csv_XY

TERMIOS = termios

class PhantomX:

    def joint_publisher(self):#, points: [[]], is_degree=None):

        pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
        rospy.init_node('joint_publisher', anonymous=False)
        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
        point = JointTrajectoryPoint()

        while True:
            key = input('Seleccione Posición o Secuencia: ')
            i=0
            if key == 'home':
                point.positions = [0, 0, 0, 0, 0]    
                point.time_from_start = rospy.Duration(0.5)
                state.points.append(point)
                pub.publish(state)
                rospy.sleep(1)

            elif key == 'marcador':
                pointer = 99
                points = (read_csv_XY(pointer,math.pi/2))
                pointArray2 = []
                for pointArray in points:

                    pointArray[4]=math.pi/2
                    point.positions = pointArray
                    point.time_from_start = rospy.Duration(0.5)
                    state.points.append(point)
                    pub.publish(state)
                    rospy.sleep(1)
                    pointArray2=pointArray
                
                #pointArray2 = [0, -math.pi/4, 0, 0, math.pi/2]  
                #point.positions = pointArray2
                #point.time_from_start = rospy.Duration(0.5)
                #state.points.append(point)
                #pub.publish(state)
                #rospy.sleep(1)
                #pass

            elif key == 'espacio':
                pointer = 49
                points = (read_csv_XY(pointer,math.pi/2))
                pointArray2 = []
                for pointArray in points:
                    point.positions = pointArray
                    point.time_from_start = rospy.Duration(0.5)
                    state.points.append(point)
                    pub.publish(state)
                    rospy.sleep(1)
                    pointArray2=pointArray
                
                pointArray2 = [0, -math.pi/2, 0, 0, math.pi/2]  
                point.positions = pointArray2
                point.time_from_start = rospy.Duration(0.5)
                state.points.append(point)
                pub.publish(state)
                rospy.sleep(1)
                pass

            elif key == 'triangulo':
                
                pointer = 0
                points =(read_csv_XY(pointer,math.pi/2))
                pointArray2 = []
                for pointArray in points:
                    print(pointArray)
                    point.positions = pointArray
                    point.time_from_start = rospy.Duration(0.5)
                    state.points.append(point)
                    pub.publish(state)
                    rospy.sleep(2)
                    time.sleep(1)
                    
                #pointArray2 = [0, -math.pi/4, 0, 0, math.pi/2] 
                #point.positions = pointArray2
                #point.time_from_start = rospy.Duration(0.5)
                #state.points.append(point)
                #pub.publish(state)
                #rospy.sleep(1)
                #pass
                
            elif key == 'j':
                
                pointer = 6
                points = read_csv_XY(pointer)
                for pointArray in points:
                    if pointArray == []:
                        dialog = input("presione a para hacer otra figura")
                        if dialog == 'a':
                            break

                    point.positions = pointArray
                    point.time_from_start = rospy.Duration(0.5)
                    state.points.append(point)
                    pub.publish(state)
                    rospy.sleep(1)

                pointArray[4] = 12
                point.positions = pointArray
                point.time_from_start = rospy.Duration(0.5)
                state.points.append(point)
                pub.publish(state)
                rospy.sleep(1)
                pass
            
            elif key == 'x':
                break
