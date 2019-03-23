import SpriteManager
from Bullet import Bullet
from PrimaryWeapon import PrimaryWeapon

class SpreadShot(PrimaryWeapon):
    wait = 1600
    mark = 0
        
    def shoot(self, vector):
        if self.cooldown:
            v1 = vector
            v2 = PVector(vector.x - 1, vector.y)
            v3 = PVector(vector.x + 1, vector.y)            
            v4 = PVector(vector.x + 2, vector.y)
            v5 = PVector(vector.x - 2, vector.y)
            SpriteManager.spawn(Bullet(self.handler.pos.x, self.handler.pos.y, v1, self.handler.team))
            SpriteManager.spawn(Bullet(self.handler.pos.x, self.handler.pos.y, v2, self.handler.team))
            SpriteManager.spawn(Bullet(self.handler.pos.x, self.handler.pos.y, v3, self.handler.team))
            SpriteManager.spawn(Bullet(self.handler.pos.x, self.handler.pos.y, v4, self.handler.team))
            SpriteManager.spawn(Bullet(self.handler.pos.x, self.handler.pos.y, v5, self.handler.team))
            self.cooldown = False
            
        if millis() - self.mark > self.wait:
            self.mark = millis()
            self.cooldown = True
