import SpriteManager

from Sprite import Sprite

class GreenZone(Sprite):
    
    wait = 7000
    maxDiameter = 120
    innerGrowthRate = 3
    innerDiameter = 0
    
    def __init__(self, x, y, team):
        Sprite.__init__(self, x, y, team)
        self.mark = millis()
    
    def display(self):
        fill(0, 255, 0, 25)
        ellipse(self.x, self.y, self.maxDiameter, self.maxDiameter)
        noFill()
        stroke(0, 100, 0, 25)
        strokeWeight(7)
        ellipse(self.x, self.y, self.innerDiameter, self.innerDiameter)
        
    def move(self):
        self.innerDiameter += self.innerGrowthRate
        if self.innerDiameter > self.maxDiameter:
            self.innerDiameter = 0
            
        if millis() - self.mark > self.wait:
            SpriteManager.destroy(self)
            
    def handleCollision(self, other):
        pass
