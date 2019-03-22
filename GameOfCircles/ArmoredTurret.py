import math
import SpriteManager

from Sprite import Sprite
from Bullet import Bullet

class ArmoredTurret(Sprite):
    
    travelSpeed = 2
    settled = False
    step = 1
    maxSteps = 100
    
    def __init__(self, startX, startY, stopX, stopY, team):
        self.pos = PVector(startX, startY)
        self.destination = PVector(stopX, stopY)
        self.wait = 50
        self.mark = millis()
        
    def aim(self, target):
        vector = PVector(target.pos.x - self.pos.x, target.pos.y - self.pos.y)
        vector.normalize()
        return vector
    
    def display(self):
        ellipse(self.destination.x, self.destination.y, 10, 10)
        ellipse(self.pos.x, self.pos.y, 20, 20)
        
    def move(self):
        if self.settled:
            if millis() - self.mark > self.wait:
                self.step = 1 if self.step > 100 else self.step + 1
                self.mark = millis()
                
                aimVector = self.aim(SpriteManager.player)
                if self.step == 1:
                    SpriteManager.spawn(Bullet(self.pos.x, self.pos.y, aimVector, self.team))
                elif self.step == 5:
                    SpriteManager.spawn(Bullet(self.pos.x, self.pos.y, aimVector, self.team))
                elif self.step == 10:
                    SpriteManager.spawn(Bullet(self.pos.x, self.pos.y, aimVector, self.team))
                
        else: # goto and stop
            xCom = self.destination.x - self.pos.x
            yCom = self.destination.y - self.pos.y
            travelVector = PVector(xCom, yCom).normalize().mult(self.travelSpeed)
            distance = self.destination.dist(self.pos)
     
            if distance > 1:
                self.pos.x += travelVector.x
                self.pos.y += travelVector.y
            else:
                self.settled = True
                self.mark = millis()
