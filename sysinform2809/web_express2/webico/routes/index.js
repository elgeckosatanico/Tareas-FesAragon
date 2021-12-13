var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'fes aragon: la mejor' });
});

router.get('/hola', function(req, res, next) {
  res.send("<h1> Hola </h1>");
});

module.exports = router;
