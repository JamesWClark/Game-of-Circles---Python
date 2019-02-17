from Sprite import Sprite

class Enemy(Sprite):
    
    speed = 8
    diameter = 50
    c = color(0,0,255)
        
    def move(self):
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1
        
