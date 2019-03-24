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
from GreenZone import GreenZone
from ArmoredTurret import ArmoredTurret

import platform
import SpriteManager

def setup():
    print "Built with Processing Python version " + platform.python_version()
    size(800, 600)
    textAlign(CENTER, CENTER)

    SpriteManager.setPlayer(Player(width / 2, height - 100, 1))
    
    startX = random(-100, width + 100)
    startY = random(-200, - 100)
    stopX = random(100, width - 100)
    stopY = random(100, height - 100)
    startX2 = random(-100, width + 100)
    startY2 = random(-200, - 100)
    stopX2 = random(100, width - 100)
    stopY2 = random(100, height - 100)
    SpriteManager.spawn(ArmoredTurret(startX, startY, stopX, stopY, 2))
    SpriteManager.spawn(ArmoredTurret(startX2, startY2, stopX2, stopY2, 2))
    
        
def draw():
    background(204)    
    SpriteManager.manage()
    
def keyPressed():
    SpriteManager.player.keyDown()    
        
def keyReleased():
    SpriteManager.player.keyUp()
    
