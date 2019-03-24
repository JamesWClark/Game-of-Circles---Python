import SpriteManager

from PrimaryWeapon import PrimaryWeapon
from BezierBullet import BezierBullet

class RandomBezierVolley(PrimaryWeapon):
    wait = 120
        
    def shoot(self, vector):
        PrimaryWeapon.shoot(self)
        x      = self.handler.pos.x
        y      = self.handler.pos.y
        team   = self.handler.team
        bullet = BezierBullet(x, y, vector.x, vector.y, team)
        SpriteManager.spawn(bullet)
