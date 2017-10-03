class Aircraft:
    def __init__(self, aircraft_type ):
        self.aircraft_type = aircraft_type
        self.ammo = 0
        if aircraft_type == "f16":
            self.max_ammo = 8
            self.base_damage = 50
        elif aircraft_type == "f35":
            self.max_ammo = 12
            self.base_damage = 50
        

    def fight(self):
        current_ammo = ammo
        self.ammo = 0
        return base_damage * current_ammo


    def refill(self, amount_of_ammo):
        if self.ammo == self.max_ammo:
            return amount_of_ammo
        if self.ammo + amount_of_ammo < self.max_ammo:
            self.ammo = self.ammo + amount_of_ammo
            return 0
        else:
                self.ammo = self.max_ammo
                return amount_of_ammo - self.max_ammo


    def get_type(self):
        return self.aircraft_type


    def get_status():
        return "Type: " + self.aircraft_type + "Ammo: " + self.ammo + "Base damage: " + self.base_damage + "All damage: " + str(self.ammo * self.base_damage)

class Carrier(object):
    def __init__(self, ammo):
        self.ammo = ammo
        self.aircrafts = []
        self.hp = hp


    def add_aircraft(self, aircraft_type):
        aircrafts.append(Aircraft(aircraft_type))
        

    def fill(self):
        if self.ammo == 0:
            raise Exception("No ammo!")   
        for aircraft in self.aircrafts:
            if aircraft.aircraft_type == "f35":
                self.ammo = aircraft.fill(self.ammo)    
        for aircraft in self.aircrafts:
            self.ammo = aircraft.refill(self.ammo)
    