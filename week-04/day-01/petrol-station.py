# Create Station and Car classes
# Station
# gas_amount
# refill(car) -> decreases the gasAmount by the capacity of the car and increases the cars gas_amount
# Car
# gas_amount
# capacity
# create constructor for Car where:
# initialize gas_amount -> 0
# initialize capacity -> 100

class Station(object):
    gas_amount = 1000000
        
class Car(object):
    gas_amount = 5
    capacity = 80
    fuel_needed = capacity - gas_amount
    def refill(self):
        Station.gas_amount -= self.fuel_needed
        Car.gas_amount += self.fuel_needed


def refill(self):
    Station.gas_amount -= self.fuel_needed
    Car.gas_amount += self.fuel_needed

Opel = Car()
Opel.refill()
Shell = Station()
print(Car.fuel_needed)
print(Station.gas_amount)


