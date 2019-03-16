from Bullet import Bullet

class Pea(Bullet):
    damage = 10
    diameter = 25
    c = color(0,255,0)
    
    def handleCollision(self, target):
        target.effects.append(GreenSlime())
