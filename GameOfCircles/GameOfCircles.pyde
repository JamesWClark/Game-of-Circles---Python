#TODO: https://stackoverflow.com/questions/13034496/using-global-variables-between-files

import platform

from Player import Player
from Bullet import Bullet
from Enemy import Enemy
from Player import Player
from Raindrop import Raindrop
from RaindropShooter import RaindropShooter
from JiggleBot import JiggleBot
from ScreenSaverBot import ScreenSaverBot

import SpriteManager

def setup():
    print "Built with Processing Python version " + platform.python_version()
    size(500, 500)
    player = Player(width / 2, height - 100, 1)
    SpriteManager.setPlayer(player)    
    SpriteManager.spawn(JiggleBot(200, 50, 2))
    SpriteManager.spawn(Enemy(100, 100, 2))
    SpriteManager.spawn(RaindropShooter(200, 200, 2))
        
def draw():
    background(255)    
    SpriteManager.animate()
    
def keyPressed():
    SpriteManager.player.keyDown()    
        
def keyReleased():
    SpriteManager.player.keyUp()
    
