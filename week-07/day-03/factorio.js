'use strict';
// - Create a function called `factorio`
//   that returns it's input's factorial

var fact = 6

function factorio(fnum) {
    let result = 1;
    for (let i=1; i <= fnum; i++) {
        result *= i;
    }
    return result
}

console.log(factorio(fact));