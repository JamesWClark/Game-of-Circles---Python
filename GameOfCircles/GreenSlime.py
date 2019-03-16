from StatusEffect import StatusEffect

class GreenSlime(StatusEffect):
    
    mark = 0
    wait = 5000
    
    def __init__(self, target):
        self.host = target
    
    def apply(self):
        self.host.velocity.x = max(2, self.host.velocity.x / 2.0)
        self.host.velocity.y = max(2, self.host.velocity.x / 2.0)
        self.host.c = color(0,255,0)
    
    def clear(self):
        self.host.velocity = self.host.__class__.velocity
        self.host.c = self.host.__class__.c
        self.host.effects.remove(self)
        
    def evaluate(self):
        self.apply()
        if(millis() - self.mark > self.wait):
            self.clear()
