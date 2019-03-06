import math

sprites = []
destroyed = []
    
playerTeam = 1
enemyTeam = 2

def setPlayer(playerInstance):
    global player
    player = playerInstance
    spawn(player)
    
def getPlayer():
    global player
    return player
        
def destroy(target):
    destroyed.append(target)
        
def spawn(obj):
    sprites.append(obj)
        
def animate():
    for sprite in sprites:
        sprite.animate()
    checkCollisions()
    bringOutYerDead()
        
def checkCollisions():
    for i in range(0, len(sprites)):
        for j in range(i + 1, len(sprites)):
            a = sprites[i]
            b = sprites[j]
            if a.team != b.team and collision(a, b):
                sprites[i].handleCollision()
                sprites[j].handleCollision()
                
def collision(a, b):
    r1 = a.diameter / 2.0
    r2 = b.diameter / 2.0
    return r1 + r2 > math.sqrt(math.pow(a.x - b.x, 2) + math.pow(a.y - b.y, 2))
                
def bringOutYerDead():
    for sprite in destroyed:
        # todo: eventally remove this if check and figure out why so many sprites get added
        if sprite in sprites: # figure out: removing this check causes like 90000 sprites to eventually add to destroyed list and multiple attempts to remove the same sprite crashes the program
            sprites.remove(sprite)
        destroyed.remove(sprite)
