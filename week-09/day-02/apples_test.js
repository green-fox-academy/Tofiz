'use strict';

var test = require('tape');
var appleClass = require('./apples.js');


test('test strings', function (t) {
    let apple = new appleClass
    t.equal(apple.getApple(), "apple");
    t.end();
  });

  test('test sum', function (t) {
    let apple = new appleClass
    t.equal(apple.sum([1, 2, 3, 4, 5]), 15); 
    t.end();
  });