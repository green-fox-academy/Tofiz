'use strict';
// - Create a variable named `abc` with the following content: `["Arthur", "Boe", "Chloe"]`
// - Swap the first and the third element of `abc`

var abc = ["Arthur", "Boe", "Chloe"]

console.log(abc[2], abc[1], abc[0]) // easy way, converted to strings

var temp = abc[2];
abc[2] = abc[0];
abc[0] = temp;

console.log(abc) // in smarter way with array