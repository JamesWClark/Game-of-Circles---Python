from Sprite import Sprite

class Raindrop(Sprite):
    speed = 8
    diameter = 50
    c = color(0, 0, 255)

    def move(self):
        self.y += self.speed
        if self.y < 0 or self.y > height:
            self.y = 0
