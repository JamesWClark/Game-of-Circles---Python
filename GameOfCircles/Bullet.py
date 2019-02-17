from Sprite import Sprite

class Bullet(Sprite):
    
    diameter = 10
    c = color(0)
    
    # constructor
    def __init__(self, x, y, vector, team):
        Sprite.__init__(self, x, y, team)
        self.vector = vector
        
    def move(self):
        self.x += self.vector.x
        self.y += self.vector.y
        
