#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

class Turtle:
    def __init__(self, turtle_name):
        self.turtle_name = turtle_name
        self.attacks = 10
        # publisher to send velocity commands
        self.vel_pub = rospy.Publisher(f'/{self.turtle_name}/cmd_vel', Twist, queue_size=10)
        # publisher for attack action
        self.attack_pub = rospy.Publisher('/attack', String, queue_size=10)
        self.vel_msg = Twist()

    def move_turtle(self, linear, angular):
        """Publish velocity command to move the turtle."""
        self.vel_msg.linear.x = linear
        self.vel_msg.angular.z = angular
        self.vel_pub.publish(self.vel_msg)



    def attack(self):
        if self.attacks > 10:
            self.attacks-=1
            self.attack_pub.publish(self.turtle_name)
            rospy.sleep(10)


    def control_loop(self):
        """main loop for controlling the turtle using the keyboard."""
        while not rospy.is_shutdown():

            command = input("press movement buttons")
            if command == 'w':
                self.move_turtle(2.0, 0.0)  # move forward
            elif command == 's':
                self.move_turtle(-2.0, 0.0)  # move backward
            elif command == 'a':
                self.move_turtle(0.0, 2.0)  # turn left
            elif command == 'd':
                self.move_turtle(0.0, -2.0)  # turn right
            elif command == 'q': # attack
                self.attack()
            else:
                self.move_turtle(0.0, 0.0)






if __name__ == "__main__":
    rospy.init_node('turtle1', anonymous=True)

    # get the node name and extract the turtle name from it
    # as each player will have a node this is his name that will be used to control the turtle
    node_name = rospy.get_name()  
    turtle_name = node_name.split('_')[0]  # turtle1 or turtle2, etc.
    turtle = Turtle(turtle_name[1:])
    pub = rospy.Publisher("/player_joined", String, queue_size=10)
    rospy.sleep(1)
    pub.publish(turtle_name[1:])

    turtle.control_loop()