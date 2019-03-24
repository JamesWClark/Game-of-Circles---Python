import SpriteManager

from Sprite import Sprite

class Armored(Sprite):
    armor = 10
    
    def display(self):
        stroke(100)
        strokeWeight(self.armor)
        fill(self.c)
        ellipse(self.pos.x, self.pos.y, self.diameter, self.diameter)
        fill(0)
        textAlign(CENTER, CENTER)
        text(self.armor, self.pos.x, self.pos.y+10)
        noStroke()
        
    def handleCollision(self, other):
        super(Armored, self).handleCollision(other)
        self.armor -= 1
        if self.armor < 1:
            SpriteManager.destroy(self)
