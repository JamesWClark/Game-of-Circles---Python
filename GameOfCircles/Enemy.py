import SpriteManager # module, not class

from Armored import Armored
from Sprite import Sprite
from Bullet import Bullet
from Shooter import Shooter

class Enemy(Armored, Shooter, Sprite):
    
    speed = 8
    c = color(0,0,255)
        
    def move(self):
        super(Enemy, self).move()
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1
