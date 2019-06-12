import SpriteManager

from Armory import Armory
from Armored import Armored
from Sprite import Sprite
from Bullet import Bullet

from Simpleton import Simpleton
from PeaShooter import PeaShooter
from SpreadShot import SpreadShot
from RandomBezierVolley import RandomBezierVolley

class Player(Armored, Sprite):
    hostile = False
    left = False
    right = False
    up = False
    down = False
    aimVector = PVector(0, -10)
    velocity = PVector(5,5)
    c = color(255,0,0)
    armory = Armory()
    damage = 15
    lives = 3
    invincible = False
    invincibleMark = 0
    
    def display(self):
        fill(self.c)
        ellipse(self.pos.x, self.pos.y, self.diameter, self.diameter)
        image(self.img, self.pos.x, self.pos.y, 50, 50)
        fill(100)
        for i in range(0, self.lives):
            ellipse(i * 20 + 20, height - 20, self.diameter, self.diameter)
    
    def handleCollision(self, other):
        if not self.invincible and self.lives > 0:
            self.c = color(255, 255, 0, 127)
            self.lives -= 1
            self.invincible = True
            self.invincibleMark = millis()
            self.pos.x = width/2
            self.pos.y = height - 100
    
    def __init__(self, x, y, team):
        Sprite.__init__(self, x, y, team)
        self.img = loadImage("rockets.png")
        
        self.armory.add(Simpleton(self))
        self.armory.add(SpreadShot(self))
        self.armory.add(PeaShooter(self))
        self.armory.add(RandomBezierVolley(self))
        self.primaryWeapon = self.armory.equip("Simpleton")
        
        
    def fire(self, vector):
        if self.hostile:
            self.primaryWeapon.shoot(vector)    
    
    def move(self):
            
        if millis() - self.invincibleMark > 1500:
            self.invincible = False
            self.c = color(255, 0, 0)
            
        if self.left:
            self.pos.x -= self.velocity.x
        if self.right:
            self.pos.x += self.velocity.x
        if self.up:
            self.pos.y -= self.velocity.y
        if self.down:
            self.pos.y += self.velocity.y
        self.pos.x = constrain(self.pos.x, self.diameter / 2, width - self.diameter / 2)
        self.pos.y = constrain(self.pos.y, self.diameter / 2, height - self.diameter / 2)
        self.fire(self.aimVector)
        
    def aim(self):
        distance = dist(mouseX, mouseY, self.x, self.y)
        xComponent = mouseX - self.x
        yComponent = mouseY - self.y
        f = 7
        return PVector(xComponent / distance * f, yComponent / distance * f)
        
    def keyDown(self):
        if key == '1':
            self.aimVector = PVector(0, -10)
            self.primaryWeapon = self.armory.equip("Simpleton")
        if key == '2':
            self.aimVector = PVector(0, -10)
            self.primaryWeapon = self.armory.equip("SpreadShot")
        if key == '3':
            self.aimVector = PVector(0, -10)
            self.primaryWeapon = self.armory.equip("PeaShooter")
        if key == '4':
            self.aimVector = PVector(self.pos.x, self.pos.y - height)
            self.primaryWeapon = self.armory.equip("RandomBezierVolley")
        
        if key == 'f' or key == 'F':
            self.hostile = True
        if keyCode == LEFT:
            self.left = True
        if keyCode == RIGHT:
            self.right = True
        if keyCode == UP:
            self.up = True
        if keyCode == DOWN:
            self.down = True
            
    def keyUp(self):
        if key == 'f' or key == 'F':
            self.hostile = False
        if keyCode == LEFT:
            self.left = False
        if keyCode == RIGHT:
            self.right = False
        if keyCode == UP:
            self.up = False
        if keyCode == DOWN:
            self.down = False
