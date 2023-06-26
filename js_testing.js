const express = require('express');
const app = express();

app.get('/', (req, res) => {
    let json = JSON.stringify({ "data": req.query.input });
    res.send(json);
});
