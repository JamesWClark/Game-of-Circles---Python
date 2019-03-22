import SpriteManager

class Sprite(object):
    hp = 100
    team = 2
    diameter = 50
    c = color(255)
    velocity = PVector(0, 0)
    damage = 0
    
    effects = []
    
    def __init__(self, x, y, team):
        self.pos = PVector(x, y)
        self.team = team
        
    def __str__(self):
        return type(self).__name__
        
    def move(self):
        pass
    
    def display(self):
        noStroke()
        fill(self.c)
        ellipse(self.pos.x, self.pos.y, self.diameter, self.diameter)
        
    def animate(self):
        for effect in self.effects:
            effect.evaluate()
        self.move()
        self.display()
        
    def isColliding(self, other):
        r1 = self.diameter / 2.0
        r2 = other.diameter / 2.0
        return r1 + r2 > dist(self.x, self.y, other.x, other.y)
    
    '''
    by default, sprites do not apply 'effects' on others. 
    leave this to concrete classes, optional
    '''
    def effect(self, other):
        pass
    
    # todo: https://stackoverflow.com/a/5268474/1161948
    def handleCollision(self, other):
        other.effect(self)
        self.hp -= other.damage
        if self.hp < 1:
            SpriteManager.destroy(self)
        
