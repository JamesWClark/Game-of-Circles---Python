import SpriteManager
from Pea import Pea

class PeaShooter:
    wait = 2400
    mark = 0
    cooldown = True
    magnitude = 2

    def __init__(self, handler):
        self.handler = handler
        
    def shoot(self, vector):
        if self.cooldown:
            self.cooldown = False
            self.mark = millis()
            vector.normalize()
            vector.x *= self.magnitude
            vector.y *= self.magnitude
            SpriteManager.spawn(Pea(self.handler.x, self.handler.y, vector, self.handler.team))
            
        if millis() - self.mark > self.wait:
            self.mark = millis()
            self.cooldown = True
