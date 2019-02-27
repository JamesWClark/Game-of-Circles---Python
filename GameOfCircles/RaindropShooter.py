import math
import SpriteManager

from Sprite import Sprite
from Raindrop import Raindrop
from Bullet import Bullet

class RaindropShooter(Raindrop):
    speed = 2
    diameter = 50
    c = color(255, 255, 0)
    mark = 0
    wait = 700

    def move(self):
        super(RaindropShooter, self).move()
        vector = self.aim(SpriteManager.getPlayer())
        self.fire(vector)
        
    def aim(self, target):
        distance = dist(target.x, target.y, self.x, self.y)
        xComponent = target.x - self.x
        yComponent = target.y - self.y
        f = 7
        if distance == 0:
            distance = 0.01
        return PVector(xComponent / distance * f, yComponent / distance * f)
            
    def fire(self, vector):
        if millis() - self.mark > self.wait:
            SpriteManager.spawn(Bullet(self.x, self.y, vector, self.team))
            self.mark = millis()
