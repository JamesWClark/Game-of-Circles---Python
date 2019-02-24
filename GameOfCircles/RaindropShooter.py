import math

import SpriteManager

from Sprite import Sprite
from Raindrop import Raindrop
from Bullet import Bullet

class RaindropShooter(Raindrop):
    speed = 2
    diameter = 50
    c = color(255, 255, 0)

    def move(self):
        super(RaindropShooter, self).move()
        vector = self.aim(SpriteManager.getPlayer())
        self.fire(vector)
        
    def aim(self, target):
        xComponent = self.x - target.x
        yComponent = self.y - target.y
        distance = math.sqrt(math.pow(xComponent, 2) + math.pow(yComponent, 2))
        xUnit = xComponent / distance
        yUnit = yComponent / distance    
        return PVector(xUnit, yUnit)
        
    def fire(self, vector):
        SpriteManager.spawn(Bullet(self.x, self.y, vector, self.team))
        
