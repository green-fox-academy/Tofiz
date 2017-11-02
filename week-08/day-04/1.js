'use strict'

function getGif (callback) {
    let httpRequest = new XMLHttpRequest()
    httpRequest.open('GET','http://api.giphy.com/v1/gifs/search?q=taylor+swift&api_key=YwfLefQAMvZEgmcKAX9scwAZzUT9vWAr&limit=16');
    httpRequest.send(null)
    httpRequest.onreadystatechange = function() {
        if(httpRequest.readyState == 4) {
            let gifs = JSON.parse(httpRequest.responseText).data
            callback(gifs)
        }
    }
}

function displayData(data) {
    data.forEach(function(gif) {
        let img = document.createElement("img")
        let url = gif.images.downsized_still.url
        let urlBig = gif.images.fixed_width.url
        img.src = url
        small.appendChild(img)
        imageEventListener(img)
    })
}

function imageEventListener(img) {
    img.addEventListener('click', function() {
        
    })
}

let big = document.querySelector(".big")
let small = document.querySelector(".small")
getGif(displayData)
