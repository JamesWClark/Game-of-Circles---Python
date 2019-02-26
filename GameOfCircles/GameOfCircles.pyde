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
    
    playerTeam = 1
    enemyTeam = 2
    player = Player(width / 2, height - 100, playerTeam);
    SpriteManager.setPlayer(player)
    
    '''
    SpriteManager.spawn(Enemy(50, 50, enemyTeam))
    SpriteManager.spawn(Enemy(150, 150, enemyTeam))
    SpriteManager.spawn(Raindrop(100, 100, enemyTeam))
    SpriteManager.spawn(JiggleBot(width/2, height/2, enemyTeam))
    SpriteManager.spawn(ScreenSaverBot(0, 0, enemyTeam))
    '''
    SpriteManager.spawn(RaindropShooter(200, 50, enemyTeam))
                           
def draw():
    background(255)    
    SpriteManager.animate()
    
def keyPressed():
    SpriteManager.player.keyDown()    
        
def keyReleased():
    SpriteManager.player.keyUp()
