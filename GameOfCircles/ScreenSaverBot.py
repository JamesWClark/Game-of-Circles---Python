from Sprite import Sprite

class ScreenSaverBot(Sprite):
    velocity = PVector(4, 2)
    c = color(0, 255, 255)

    def move(self):
        self.x += self.velocity.x
        self.y += self.velocity.y
        if self.x < 0 or self.x > width:
            self.velocity.x *= -1
        if self.y < 0 or self.y > height:
            self.velocity.y *= -1
    
