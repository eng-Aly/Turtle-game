#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from std_msgs.msg import String
import math
from turtlesim.srv import Kill

players_data = {"turtle1":{'x':None ,'y':None ,'theta':None, "health":100}}
gameover = True

def setPosition(position,name):
    players_data[name]={'x':position.x ,'y':position.y ,'theta':position.theta}

def positionHandler(name):
    rospy.Subscriber(f'/{name}/pose',Pose,setPosition,name)


def handler(msg):
    name = msg.data
    if name not in players_data.keys():
        players_data[name]={name:{'x':None ,'y':None ,'theta':None, "health":100}}

        positionHandler(name)

def attacking(msg):
    attacker = msg.data
    positionHandler(attacker)
    for target in players_data.keys():
        positionHandler(target)
        distance = math.sqrt((players_data[attacker]['x'] - players_data[target]['x']) ** 2 +
                                    (players_data[attacker]['y'] - players_data[target]['y']) ** 2)
        if distance < 2.0:
            players_data[target]["health"] -= 50

            if players_data[target]["health"] == 0:
                rospy.wait_for_service('/kill')
                try:
                    kill = rospy.ServiceProxy('/kill',Kill)
                    kill(target)
                    rospy.logwarn(f"{target} has been defeated")
                    players_data.pop(target)

                except rospy.ServiceException as e:
                    rospy.logger(f"Service call failed: {e}")

    if len(players_data) == 1:
        rospy.loginfo(f"{attacker}have won!!")
        gameover = False






if __name__ == "__main__":
    rospy.init_node('turtle_observer')
    rospy.loginfo("observer is runing...")
    prev1 = None
    rospy.Subscriber("/player_joined", String , handler)
    rospy.Subscriber("/attack", String,attacking)
    while not rospy.is_shutdown() and gameover:
        print (players_data)