var express = require('express');
var app = express();

express.json.type = "application/json"

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

    app.listen(8080);