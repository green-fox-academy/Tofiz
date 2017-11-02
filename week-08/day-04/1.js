'use strict'



function getGif (callback) {
    let httpRequest = new XMLHttpRequest();
    httpRequest.open('GET','http://api.giphy.com/v1/gifs/search?q=taylor+swift&api_key=YwfLefQAMvZEgmcKAX9scwAZzUT9vWAr&limit=16');
    httpRequest.send(null)
    httpRequest.onreadystatechange = function() {
        if(httpRequest.readyState == 4) {
            let gifs = JSON.parse(httpRequest.responseText).data
            callback(gifs);
        }
    }
}

function displayData(data) {
    data.forEach(function(gif) {
        let img = document.createElement("img");
        let url = gif.images.downsized_still.url;
        img.src = url;
        body.appendChild(img);
    });
}

let body = document.querySelector("body")
let a = getGif(displayData)

