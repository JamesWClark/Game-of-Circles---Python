from Sprite import Sprite

from Armored import Armored

class JiggleBot(Armored, Sprite):
    armor = 4
    velocity = PVector(4, 4)
    diameter = 20
    c = color(100, 100, 255)

    def move(self):
        self.x += random(-self.velocity.x, self.velocity.x)
        self.y += random(-self.velocity.y, self.velocity.y)
        self.x = constrain(self.x, 0, width)
        self.y = constrain(self.y, 0, height)
