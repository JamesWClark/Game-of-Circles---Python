import SpriteManager

from Bullet import Bullet
from Sprite import Sprite

class Shooter:
    
    mark = 0
    wait = 700
    
    def move(self):
        vector = self.aim(SpriteManager.getPlayer())
        self.fire(vector)
        
    def aim(self, target):
        
        # right triangle vector
        distance = dist(target.x, target.y, self.x, self.y)
        xComponent = target.x - self.x
        yComponent = target.y - self.y
        
        # prevents divide by zero when units exactly overlap on x,y
        if distance == 0: 
            distance = 0.01
            
        # return unit vector * magnitude
        magnitude = 7
        return PVector(xComponent / distance * magnitude, yComponent / distance * magnitude)
            
    def fire(self, vector):
        if millis() - self.mark > self.wait:
            SpriteManager.spawn(Bullet(self.x, self.y, vector, self.team))
            self.mark = millis()
