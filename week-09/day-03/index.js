var express = require('express');
var app = express();

express.json.type = "application/json"

app.use(express.json())

app.use('/assets', express.static('./assets'));


app.get('/', function(req, res){
    res.sendFile(__dirname + '/index.html');
});


app.get('/doubling', function(req, res){
    let input = req.query.input;
    if (input != null) {
        res.send({
            "received": input,
            "result": input * 2
        })
    } else {
        res.send({"error":"Please provide an input!"
        })

    }
});
    

app.get('/greeter', function(req, res){
    let nameQuery = req.query.name;
    let titleQuery = req.query.title;
    if (nameQuery == null) {
        res.send({
            "error": "Please provide a name!"
        })
    } else if (titleQuery == null) {
        res.send({
            "error": "Please provide a title!"
        })
    } else {
        res.send({
            "welcome_message": "Oh, hi there " + nameQuery + ", my dear " + titleQuery + "!"
        })
    }
});

app.get('/appenda/:anything', function(req, res){
    res.send({
        "appended": req.params.anything + 'a'
    })
});

app.post('/dountil/:what', function(req, res){
    if (req.params.what == "sum") {
       let sum = 0
       for ( let i = 0; i <= req.body.until; i++) {
           sum += i
        }
        res.send({ "result": sum})
        
    } else if (req.params.what == "factor") {
        let sum = 1
    for ( let i = 1; i <= req.body.until; i++) {
        sum = sum * i
    }
    res.send({ "result": sum})
    } else {
       res.send({"error": "Please provide a number!"}) 
    } 
});


app.listen(8080);