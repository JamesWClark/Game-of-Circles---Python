import platform
import SpriteManager

from Bullet import Bullet
from Enemy import Enemy
from Player import Player

def setup():
    print "Built with Processing Python version " + platform.python_version()
    size(800, 600)
    textAlign(CENTER, CENTER)

    SpriteManager.setPlayer(Player(width / 2, height - 100, 1))

    SpriteManager.spawn(Enemy(100, 100, 2)) 
        
def draw():
    background(204)    
    SpriteManager.manage()
    
def keyPressed():
    SpriteManager.player.keyDown()    
        
def keyReleased():
    SpriteManager.player.keyUp()
    
