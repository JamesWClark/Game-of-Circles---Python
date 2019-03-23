import SpriteManager

from Bullet import Bullet
from GreenSlime import GreenSlime
from GreenZone import GreenZone

class Pea(Bullet):
    diameter = 15
    c = color(0,255,0)
    damage = 0
    
    '''
    def effect(self, other):
        other.effects.append(GreenSlime(other))
       '''
        
    def handleCollision(self, other):
        SpriteManager.spawn(GreenZone(self.pos.x, self.pos.y, self.team))
        SpriteManager.destroy(self)
