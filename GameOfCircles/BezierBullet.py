import SpriteManager

from Sprite import Sprite

class BezierBullet(Sprite):
    damage = 34
    c = color(255)
    diameter = 20
    t = 0
    
    def __init__(self, x1, y1, x4, y4, team):
        Sprite.__init__(self, x1, y1, team)
        # self.pos.x = bezierPoint(self.x1, self.x2, self.x3, self.x4, self.t);
        # self.pos.y = bezierPoint(self.y1, self.y2, self.y3, self.y4, self.t);
        self.x1 = x1
        self.y1 = y1
        self.x2 = random(min(x1, x4), max(x1, x4))
        self.y2 = random(min(y1, y4), max(y1, y4))
        self.x3 = random(min(x1, x4), max(x1, x4))
        self.y3 = random(min(y1, y4), max(y1, y4))
        self.x4 = x4
        self.y4 = y4


    def move(self):
        self.t += 0.01
        self.pos.x = bezierPoint(self.x1, self.x2, self.x3, self.x4, self.t);
        self.pos.y = bezierPoint(self.y1, self.y2, self.y3, self.y4, self.t);
        
        if self.pos.x < 0 or self.pos.x > width:
            SpriteManager.destroy(self)

        if self.pos.y < 0 or self.pos.y > height:
            SpriteManager.destroy(self)
