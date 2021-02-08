let express = require('express');
let mysql = require('mysql');
let bodyParser = require('body-parser');
let app = express();

app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static(__dirname + "/public"));

let connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  database : 'join_us'
});
 
app.get("/", function(req, res){
 let q = 'SELECT COUNT(*) as count FROM users';
 connection.query(q, function (err, results) {
 if (err) throw err;
 let count = results[0].count;
 res.render("home", {data : count});
 })
});

app.post("/register", function(req, res){
 let person = {email: req.body.email};
 connection.query('INSERT INTO users SET ?', person, function(err, result) {
 if (err) throw err
 res.redirect("/");
 });
});
	
app.get("/joke", function(req, res){
 let joke = "What do you call a dog that does magic tricks? A labracadabrador.";
 res.send(joke);
});

app.get("/random_num", function(req, res){
 let num = Math.floor((Math.random() * 10) + 1);
 res.send("Your lucky number is " + num);
});
 
app.listen(3000, function () {
 console.log('App listening on port 3000!');
});