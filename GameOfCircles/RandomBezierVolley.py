import SpriteManager

from PrimaryWeapon import PrimaryWeapon
from BezierBullet import BezierBullet

class RandomBezierVolley(PrimaryWeapon):
    wait = 120
        
    def shoot(self, vector):
        
        SpriteManager.spawn(BezierBullet(self.handler.pos.x, self.handler.pos.y, vector.x, vector.y, self.handler.team))
        
        if self.cooldown:
            self.cooldown = False
            self.mark = millis()

        if millis() - self.mark > self.wait:
            self.mark = millis()
            self.cooldown = True
            
            
