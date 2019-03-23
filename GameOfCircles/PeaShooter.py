import SpriteManager
from Pea import Pea
from PrimaryWeapon import PrimaryWeapon

class PeaShooter(PrimaryWeapon):
    magnitude = 6
        
    def shoot(self, vector):
        if self.cooldown:
            self.cooldown = False
            self.mark = millis()
            vector.normalize()
            vector.x *= self.magnitude
            vector.y *= self.magnitude
            SpriteManager.spawn(Pea(self.handler.pos.x, self.handler.pos.y, vector, self.handler.team))
            
        if millis() - self.mark > self.wait:
            self.mark = millis()
            self.cooldown = True
