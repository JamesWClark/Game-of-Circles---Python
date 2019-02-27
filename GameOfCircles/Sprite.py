import SpriteManager

class Sprite(object):
    team = 2
    diameter = 50
    c = color(255)
    
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        
    def __str__(self):
        return type(self).__name__
        
    def move(self):
        pass
    
    def display(self):
        fill(self.c)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
    def animate(self):
        self.move()
        self.display()
        
    def isColliding(self, other):
        r1 = self.diameter / 2.0
        r2 = other.diameter / 2.0
        return r1 + r2 > dist(self.x, self.y, other.x, other.y)
    
    def handleCollision(self):
        SpriteManager.destroy(self)
