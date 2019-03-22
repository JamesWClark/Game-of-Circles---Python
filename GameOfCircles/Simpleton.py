import SpriteManager
from Bullet import Bullet

class Simpleton:
    wait = 120
    mark = 0
    cooldown = True
    magnitude = 12

    def __init__(self, handler):
        self.handler = handler
        
    def shoot(self, vector):
        if self.cooldown:
            self.cooldown = False
            self.mark = millis()
            vector.normalize()
            vector.x *= self.magnitude
            vector.y *= self.magnitude
            SpriteManager.spawn(Bullet(self.handler.pos.x, self.handler.pos.y, vector, self.handler.team))
            
        if millis() - self.mark > self.wait:
            self.mark = millis()
            self.cooldown = True
