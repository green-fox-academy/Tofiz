'use strict';

// An average Green Fox attendee codes 6 hours daily
// The semester is 17 weeks long
//
// Print how many hours is spent with coding in a semester by an attendee,
// if the attendee only codes on workdays.
//
// Print the percentage of the coding hours in the semester if the average
// work hours weekly is 52


function coding_hours () {
    let working_hours = 6 * 5 * 17;
    console.log (working_hours);
    let percentage = (working_hours / (52 * 17)) * 100;
    console.log(percentage + '%')
}

coding_hours()