import math
import SpriteManager

from Armored import Armored
from Sprite import Sprite
from RandomBezierVolley import RandomBezierVolley

class ArmoredTurret(Armored):
    
    travelSpeed = 2
    settled = False
    step = 1
    maxSteps = 40
    c = color(155, 155, 0)
    
    def __init__(self, startX, startY, stopX, stopY, team):
        self.pos = PVector(startX, startY) # current position
        self.dest = PVector(stopX, stopY)  # target destination
        self.wait = 50
        self.mark = millis()
        self.primaryWeapon = RandomBezierVolley(self)
        
    def aim(self, target):
        vector = PVector(target.pos.x - self.pos.x, target.pos.y - self.pos.y)
        vector.normalize()
        return vector
    
    def display(self):
        Armored.display(self)

        # landing pad
        x = self.dest.x
        y = self.dest.y
        offset = self.diameter / 5
        stroke(0)
        strokeWeight(1)
        line(x - offset, y, x + offset, y) # horizontal
        line(x, y - offset, x, y + offset) # vertical 
        noFill()
        ellipse(x, y, offset, offset)
        # noStroke()
        
    def move(self):
        if self.settled:
            if millis() - self.mark > self.wait:
                self.step = 1 if self.step > self.maxSteps else self.step + 1
                self.mark = millis()
                
                if self.step == 1:
                    self.primaryWeapon.shoot(SpriteManager.player.pos)
                elif self.step == 5:
                    self.primaryWeapon.shoot(SpriteManager.player.pos)
                elif self.step == 10:
                    self.primaryWeapon.shoot(SpriteManager.player.pos)
                elif self.step == 15:
                    self.primaryWeapon.shoot(SpriteManager.player.pos)
                elif self.step == 20:
                    self.primaryWeapon.shoot(SpriteManager.player.pos)
                
        else: # goto and stop
            xCom = self.dest.x - self.pos.x
            yCom = self.dest.y - self.pos.y
            travelVector = PVector(xCom, yCom).normalize().mult(self.travelSpeed)
            distance = self.dest.dist(self.pos)
     
            if distance > 1:
                self.pos.x += travelVector.x
                self.pos.y += travelVector.y
            else:
                self.settled = True
                self.mark = millis()
