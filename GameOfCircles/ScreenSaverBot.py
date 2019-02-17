from Sprite import Sprite

class ScreenSaverBot(Sprite):
    xspeed = 8
    yspeed = 4
    diameter = 50
    c = color(0, 255, 255)

    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        if self.x < 0 or self.x > width:
            self.xspeed *= -1
        if self.y < 0 or self.y > height:
            self.yspeed *= -1
    
