
from Sprite import Sprite
    
class OddBall(Sprite):
    
    c = color(0,255,0)
    
    # override Sprite constructor
    def __init__(self, x, y, diameter, team):
        Sprite.__init__(self, x, y, team)
        self.diameter = diameter
        
    def move(self):
        ellipse(self.x, self.y, self.diameter, self.diameter)
    
