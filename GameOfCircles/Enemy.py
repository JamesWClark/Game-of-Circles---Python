import SpriteManager # module, not class

from Armored import Armored
from Sprite import Sprite
from Bullet import Bullet
from Shooter import Shooter

class Enemy(Armored, Shooter, Sprite):
    
    velocity = PVector(8, 0)
    c = color(0,0,255)
        
    def move(self):
        super(Enemy, self).move()
        self.x += self.velocity.x
        if self.x < 0 or self.x > width:
            self.velocity.x *= -1
