class PrimaryWeapon:
    wait = 400
    mark = 0
    cooldown = True

    def __init__(self, handler):
        self.handler = handler
    
    def shoot(self):
        if self.cooldown:
            self.cooldown = False
            self.mark = millis()

        if millis() - self.mark > self.wait:
            self.mark = millis()
            self.cooldown = True
            
            
