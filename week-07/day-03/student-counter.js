'use strict';

var students = [
        {'name': 'Teodor', 'age': 3, 'candies': 2},
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
    ];

// create a function that takes a list of students and logs: 
// - how many candies are owned by students

// create a function that takes a list of students and logs:
// - Sum of the age of people who have lass than 5 candies


function how_many_candies_they_have() {
    var owned_candies = 0
    for (let i = 0; i < students.length; i++) {
        owned_candies += students[i].candies;
    };
    return owned_candies
}


function sum_of_the_age_who_have_lass_than_5() {
    var ages = 0
    for (let i = 0; i < students.length; i++) {
        if (students[i].candies < 5) {
            ages += students[i].age
            
        }
    }
    return ages
}
console.log(how_many_candies_they_have())
console.log(sum_of_the_age_who_have_lass_than_5())
