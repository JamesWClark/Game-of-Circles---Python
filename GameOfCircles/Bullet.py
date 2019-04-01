import SpriteManager

from Sprite import Sprite

class Bullet(Sprite):
    damage = 34
    diameter = 5
    c = color(0)
    
    # constructor
    def __init__(self, x, y, velocity, team):
        Sprite.__init__(self, x, y, team)
        self.velocity = velocity
        
    def move(self):
        self.pos.add(self.velocity)
        
        if (self.pos.x < 0 - self.diameter
        or self.pos.x > width + self.diameter
        or self.pos.y < 0 - self.diameter
        or self.pos.y > height + self.diameter):
            SpriteManager.destroy(self)
