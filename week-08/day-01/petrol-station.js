'use strict';
// Create and object called car
//  - It should store its petrol level called petrolLevel
//  - It should store its petrol capacity called petrolCapacity
//  - It should have a refill(amount) method, that increments the petrol level,
//    than returns how much petrol it consumed from the given amount
//  - Initialize the petrol level to zero and the capacity to 50 
//
// Create an object called station
//  - It should store petrol amount called petrolStorage
//  - It should have a provide(car) method that calls the refill method of the car
//    with the stored petrol amount as a parameter, then decrement the used petrol
//  - Initialize the petrol amount to 3000

let car = {
    petrolLevel: 0,
    petrolCapacity: 50,
    refill: function(amount) {
        if (this.petrolLevel + amount > this.petrolCapacity) {
            let consumedAmount = this.petrolCapacity - this.petrolLevel;
            this.petrolLevel = this.petrolCapacity;
            return consumedAmount;
        } else {
            this.petrolLevel += amount;
            return amount;
        }
    }
}

// car.refill(10)


let station = {
    petrolStorage: 3000,
    provide: function(car) {
        car.refill(this.petrolStorage);
        let consumedAmount = this.petrolCapacity - this.petrolLevel;
        this.petrolStorage -= car.consumedAmount;
        return petrolStorage;
    }

}


console.log(car.petrolLevel + " is the current petrol level of the car.");
console.log(station.petrolStorage + " is the current amount of the petrol station storage.");

station.provide(car);

console.log(car.petrolLevel + " is the current petrol level of the car after refilling it.") ;
console.log(station.petrolStorage + " is current station petrol level after refilling the car.");
// console.log(amount)