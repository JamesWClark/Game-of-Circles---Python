import SpriteManager

from Bullet import Bullet
from GreenSlime import GreenSlime

class Pea(Bullet):
    hp = 0
    diameter = 25
    c = color(0,255,0)
    damage = 0
    
    def effect(self, other):
        other.effects.append(GreenSlime(other))
