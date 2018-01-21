var express = require('express');
var app = express();
var path = require('path');

// viewed at http://localhost:8080
app.get('/', function(req, res) {
  console.log('GET index.html');
  res.sendFile(path.join(__dirname + '/index.html'));
});

console.log('Server running on port 8080');
app.listen(8080);
