import SpriteManager

from PrimaryWeapon import PrimaryWeapon
from BezierBullet import BezierBullet

class RandomBezierVolley(PrimaryWeapon):
    wait = 120
        
    def shoot(self, vector):
        x      = self.handler.pos.x
        y      = self.handler.pos.y
        team   = self.handler.team
        
        bullet = BezierBullet(x, y, vector.x, vector.y, team)
        SpriteManager.spawn(bullet)
        
        if self.cooldown:
            self.cooldown = False
            self.mark = millis()

        if millis() - self.mark > self.wait:
            self.mark = millis()
            self.cooldown = True
            
            
