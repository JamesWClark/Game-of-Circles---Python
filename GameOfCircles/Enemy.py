from Sprite import Sprite


class Enemy(Sprite):
    
    velocity = PVector(8, 0)
    c = color(0,0,255)
        
    def move(self):
        super(Enemy, self).move()
        self.pos.add(self.velocity)
        if self.pos.x < 0 or self.pos.x > width:
            self.velocity.x *= -1
