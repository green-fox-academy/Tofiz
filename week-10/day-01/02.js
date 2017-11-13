'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference




function Rectangles(A, B) {
    this.A = A; 
    this.B = B; 
}

Rectangles.prototype.getArea = function () {
    let area = this.A * this.B;
    return area
}

Rectangles.prototype.getCircumference = function (A, B) {
    let Circumference =  2 * (this.A + this.B);
    return Circumference
}





var square = new Rectangles(5, 5)

console.log(square.getArea())
console.log(square.getCircumference())