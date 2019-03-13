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
        distance = dist(target.x, target.y, self.x, self.y)
        xComponent = target.x - self.x
        yComponent = target.y - self.y
        if distance == 0: 
            distance = 0.01
        magnitude = 7
        return PVector(xComponent / distance * magnitude, yComponent / distance * magnitude)
            
    def fire(self, vector):
        if millis() - self.mark > self.wait:
            SpriteManager.spawn(Bullet(self.x, self.y, vector, self.team))
            self.mark = millis()
