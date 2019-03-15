from Sprite import Sprite

from Armored import Armored

class JiggleBot(Armored, Sprite):
    armor = 4
    speed = 4
    diameter = 20
    c = color(100, 100, 255)

    def move(self):
        self.y += random(-self.speed, self.speed)
        self.x += random(-self.speed, self.speed)
        self.x = constrain(self.x, 0, width)
        self.y = constrain(self.y, 0, height)
