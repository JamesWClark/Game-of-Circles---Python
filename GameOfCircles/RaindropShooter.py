import math
import SpriteManager

from Shooter import Shooter
from Raindrop import Raindrop
from Bullet import Bullet

class RaindropShooter(Raindrop, Shooter):
    speed = 2
    c = color(255, 255, 0)
    mark = 0
    wait = 700

    def move(self):
        Raindrop.move(self)
        Shooter.move(self)
