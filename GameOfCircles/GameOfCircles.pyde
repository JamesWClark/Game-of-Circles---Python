from Player import Player
from Bullet import Bullet
from Enemy import Enemy
from Player import Player
from Raindrop import Raindrop
from RaindropShooter import RaindropShooter
from JiggleBot import JiggleBot
from ScreenSaverBot import ScreenSaverBot
from OddBall import OddBall
from Armored import Armored

import platform
import SpriteManager

def setup():
    print "Built with Processing Python version " + platform.python_version()
    size(500, 500)

    SpriteManager.setPlayer(Player(width / 2, height - 100, 1))    
    SpriteManager.spawn(JiggleBot(200, 50, 2))
    SpriteManager.spawn(Enemy(100, 100, 2))
    SpriteManager.spawn(RaindropShooter(200, 200, 2))
    SpriteManager.spawn(OddBall(100, 100, 50, 2))
    SpriteManager.spawn(OddBall(200, 100, 40, 2))
    SpriteManager.spawn(OddBall(100, 200, 20, 2))
    
        
def draw():
    background(204)    
    SpriteManager.manage()
    
def keyPressed():
    SpriteManager.player.keyDown()    
        
def keyReleased():
    SpriteManager.player.keyUp()
    
