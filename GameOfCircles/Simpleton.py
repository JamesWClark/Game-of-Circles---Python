import SpriteManager
from Bullet import Bullet
from PrimaryWeapon import PrimaryWeapon

class Simpleton(PrimaryWeapon):
    wait = 250
    magnitude = 12
        
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
