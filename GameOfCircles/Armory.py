class Armory:
    weapons = {} # dictionary

    def add(self, weapon):
        name = weapon.__class__.__name__
        self.weapons[name] = weapon
        
    def remove(self, weapon):
        if weapon in self.weapons:
            self.weapons.pop(weapon)
        
    def equip(self, weapon):
        return self.weapons[weapon]
