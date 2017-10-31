'use strict'
// Create a prison function, that has your name as a private fugitive variable
// The function should return an object that has two methods:
//   - visit() // logs "[yourname] is visited [x] time(s)" to the console.
//    - the [x] times displayes the numbers the function is called
//    - If the fugitive variable is empty, then display "Nobody is here anymore"
//   - escape() // logs "BREAKING NEWS, [yourname] escaped the prison" to the console.
//    - it should empties the fugitive variable

function prison(name) {
    var times = 0;
    var fugitive = [name];
    function visit() {
        if (fugitive.length == 0){
            console.log('Nobody is here anymore')
        } else 
        console.log(fugitive[0] + ' is visitted ' + times + ' time(s)')
        times++;

    }
    function escape() {
    console.log("BREAKING NEWS, "+ fugitive[0] + " escaped the prison")
    fugitive = [];
    }
return {
    visit: function(){
        visit()},
    escape: function() {
        escape()}
}
    
}



const alcatraz = prison('Sad Panda') 


alcatraz.visit() // Sad Panda is visited 1 time(s)
alcatraz.visit() // Sad Panda is visited 2 time(s)
alcatraz.escape() // BREAKING NEWS, Sad Panda escaped the prison
alcatraz.visit() // Nobody is here anymore