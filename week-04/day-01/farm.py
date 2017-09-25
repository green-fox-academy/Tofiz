# Reuse your Animal class
# Create a Farm class
# it has list of Animals
# it has slots which defines the number of free places for animals
# breed() -> creates a new animal if there's place for it
# slaughter() -> removes the least hungry animal

class Animal(object):
    
    def __init__(self):
        self.hunger = 50
        self.thirst = 50

    def eat(self):
        self.hunger -= 1
        return print(self.hunger)
    
    def drink(self):
        self.thirst -= 1
        return print(self.thirst)

    def play(self):
        self.hunger += 1
        self.thirst += 1
        return print("hungry" , str(self.hunger), "thirsty", str(self.thirst))

class Farm(object):
    animals = []
    slots = 200
    print(slots - len(animals))
    def __init__(self):
        self.hunger = 50
        self.thirst = 50

    def breed():