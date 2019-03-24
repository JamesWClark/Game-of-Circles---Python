import math

active = []
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
    active.append(obj)
        
def manage():
    updatePositions()
    checkCollisions()
    bringOutYerDead()
        
def updatePositions():
    for i in range(len(active)-1, -1, -1):
        active[i].animate()


def checkCollisions():
    for i in range(0, len(active)):
        for j in range(i + 1, len(active)):
            a = active[i]
            b = active[j]
            if a.team != b.team and collision(a, b):
                a.handleCollision(b)
                b.handleCollision(a)
                
def collision(a, b):
    r1 = a.diameter / 2.0
    r2 = b.diameter / 2.0
    return r1 + r2 > math.sqrt(math.pow(a.pos.x - b.pos.x, 2) + math.pow(a.pos.y - b.pos.y, 2))
                
def bringOutYerDead():
    for sprite in destroyed:
        if sprite in active: # figure out: removing this check causes like 90000 active to eventually add to destroyed list and multiple attempts to remove the same sprite crashes the program
            active.remove(sprite)
        destroyed.remove(sprite)
