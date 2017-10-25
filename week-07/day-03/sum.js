'use strict';
// - Write a function called `sum` that sum all the numbers until the given parameter
// - The function should return the result

var givenParameter = 76

function sum(gp) {
    let result = 0;
    for (let i=1; i <= gp; i++) {
        result += i;
    }
    return result
}

console.log(sum(givenParameter));