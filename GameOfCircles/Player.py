import SpriteManager

from Sprite import Sprite
from Bullet import Bullet

class Player(Sprite):
    
    left = False
    right = False
    up = False
    down = False
    speed = 5
    diameter = 50
    c = color(255,0,0)
        
    def move(self):
        if self.left:
            self.x -= self.speed
        if self.right:
            self.x += self.speed
        if self.up:
            self.y -= self.speed
        if self.down:
            self.y += self.speed
        self.x = constrain(self.x, self.diameter / 2, width - self.diameter / 2)
        self.y = constrain(self.y, self.diameter / 2, height - self.diameter / 2)
        
    def aim(self):
        distance = dist(mouseX, mouseY, self.x, self.y)
        xComponent = mouseX - self.x
        yComponent = mouseY - self.y
        f = 7
        return PVector(xComponent / distance * f, yComponent / distance * f)
        
    def fire(self, vector = None):
        if vector is None:
            SpriteManager.spawn(Bullet(self.x, self.y, PVector(0, -10), self.team))
        else:
            SpriteManager.spawn(Bullet(self.x, self.y, vector, self.team))
            
    # player overrides Sprite.handleCollision, thus making himself invincible by passing through
    def handleCollision(self):
        pass
        
    def keyDown(self):
        if key == 'f' or key == 'F':
            self.fire()
        if keyCode == LEFT:
            self.left = True
        if keyCode == RIGHT:
            self.right = True
        if keyCode == UP:
            self.up = True
        if keyCode == DOWN:
            self.down = True
            
    def keyUp(self):
        if keyCode == LEFT:
            self.left = False
        if keyCode == RIGHT:
            self.right = False
        if keyCode == UP:
            self.up = False
        if keyCode == DOWN:
            self.down = False
