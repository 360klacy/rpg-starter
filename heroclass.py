


class hero():
    def __init__(self, health, power,):
        self.health = health
        self.power = power
    def alive(self):
        return self.health > 0  
    def attack(self, victim): 
        victim.health -= self.power  
    def print_Status(self):
        print('You have' + str(self.health) + 'left')


class goblin(hero):
    def __init__(self, health, power):
        super().__init__(health, power)        
        

    # def attack(self, hero):
    #     hero.health -= self.power
    




    