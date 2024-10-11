import express from 'express';

const app = express();
const port = 1245;

app.get("/", (req, res) => {
    res.send('Hello Holberton School!');
})

app.listen(port, () => {
    console.log('Server is listening on port 1245!');
})