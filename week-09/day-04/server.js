'use strict'

var express = require('express');
var app = express();

app.use(express.json())
app.use('/assets', express.static('./assets'))
express.json.type = "application/json"

var mysql = require("mysql");

var conn = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "root",
  database: 'bookstore'
});

conn.connect(function(err){
  if(err){
    console.log("Error connecting to Db");
  } else {
  console.log("Connection established"); }
});

app.get('/', function(req,res){
  res.sendFile(__dirname + '/index.html');
});

app.get('/list', function(req, res){
  conn.query('SELECT book_name FROM book_mast;', function(err, rows){
      if(err) {
          console.log(err.toString());
      }
      console.log("Data received from Db:\n");
      let htmlString = '<ol>';
      rows.forEach(function(row) {
          htmlString = htmlString + '<li>' + row.book_name + '</li>';
      });
      htmlString = htmlString + '</ol>';
      res.send(htmlString)
  });
});

app.listen(8080)