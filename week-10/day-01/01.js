'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says

function Animals(sound) {
    this.sound = sound;  //this is the constructor
}

Animals.prototype.says = function(sound) {
    console.log(this.sound) //this is what they say
}

var cat = new Animals("Miaouuuuh")
var dog = new Animals("Whuff")
var elephant = new Animals("Mhouuuuuu")


cat.says()
dog.says()
elephant.says()
