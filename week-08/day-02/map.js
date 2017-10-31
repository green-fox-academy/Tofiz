'use strict'

var fruits = [
  'melon',
  'apple',
  'strawberry',
  'blueberry',
  'pear',
  'banana'
];

// Create a new array of consists numbers that shows how many times the 'e' letter
// occurs in the word stored under the same index at the fruits array!
// Please use the map method.

var eInWords = fruits.map(function(x) {
    var counter = 0;
    for (let i = 0; i <= x.length ; i++ ) {
        if ( x[i] === "e" ) {
            counter ++;
        }
    }
    return counter;
});

console.log(eInWords);