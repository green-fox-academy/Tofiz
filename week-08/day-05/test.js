function doRequest(callback) {
    var x = new XMLHttpRequest();
    x.open('GET', 'https://cors-anywhere.herokuapp.com/http://secure-reddit.herokuapp.com/posts');
    x.onload = function() {
        callback(x.responseText)
    };
    x.send();
}

function handleData(data){
    console.log(data);
}

doRequest(handleData)