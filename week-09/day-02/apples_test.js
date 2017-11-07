'use strict';

var test = require('tape');
var apple = require('./apples.js');


test('test strings', function (t) {
    t.equal(apple.getApple(), "apple");
    t.end();
  });