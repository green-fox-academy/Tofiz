'use strict';
// - Create a variable named `nimals`
//   with the following content: `["kuty", "macsk", "cic"]`
// - Add all elements an `"a"` at the end
// - try to use built in functions instead of loops

var nimals = ["kuty", "macsk", "cic", "alm", "bik", "zebraaaa"]

nimals.forEach(function(x,i) {
    nimals[i] += 'a';
})

console.log(nimals);