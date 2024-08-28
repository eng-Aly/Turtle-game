  #!/usr/bin/env python3 
import rospy

class player :
    def __init__(self) :
        self.hp = 100
        self.attacks = 10
        self.damage = 50

    def attack(self,target) :
        if self.attacks > 0 :
            target.hp -=  self.damage
            self.attacks -= 1

    def aliveflag () :
        return self.hp > 0       

        

    
