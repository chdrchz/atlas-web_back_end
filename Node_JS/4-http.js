import express from 'express';
import http from 'http';

var app = express();
var port = 1245;

// Create an HTTP service.
http.createServer(app).listen(port, () => {
    console.log(`Server running on port ${port}`);
});

// Define a route to handle GET requests
app.get("/", (req, res) => {
    res.send("Hello Holberton School!");
});
