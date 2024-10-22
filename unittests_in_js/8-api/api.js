const express = require('express');

const app = express();
const port = 7865;

const server = app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});

app.get("/", (req, res) => {
    res.send('Welcome to the payment system');
});

module.exports = { app, server };