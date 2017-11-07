'use strict';

class apple { 
    getApple() {
    return "apple"
    }


    sum(numArray) {
        let summa = numArray.reduce(function(sum, value) {
            return sum + value
        });
        return summa;
        }
};

module.exports = apple;
