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
    
    def handleCollision(self, other):
        pass
    
    def __init__(self, x, y, team):
        Sprite.__init__(self, x, y, team)
        self.armory.add(Simpleton(self))
        self.armory.add(SpreadShot(self))
        self.armory.add(PeaShooter(self))
        self.armory.add(RandomBezierVolley(self))
        self.primaryWeapon = self.armory.equip("Simpleton")
        
    def fire(self, vector):
        if self.hostile:
            self.primaryWeapon.shoot(vector)    
    
    def move(self):
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
