var config = require('./config.json');
var rest = require('exprestify')
/* Twitter Functionality */
var Twitter = require('node-tweet-stream')
  , t = new Twitter({
    consumer_key:config.ckey,
    consumer_secret:config.csec,
    token:config.otoken ,
    token_secret:config.osec
  });
 
/* Server */
var header ={
"Access-Control-Allow-Origin":"*", //Restrict it to the origin of your server
"Access-Control-Allow-Methods":"GET,PUT,POST,DELETE",
"Access-Control-Allow-Headers":"Content-Type"
};

rest.setHeaders(header);
rest.getfile('/', function (err, query) { 
	if (!err) {
		return "./index.html"; 
	} 
	else { 
		console.log(err); 
		return err; 
	} 
})

rest.get('/tweet', function (err, query) {
        if (!err) {
                t.track(query.search);
                return "done";
        }
        else {
                console.log(err);
                return err;
        }
});

var server = rest.getSocketServer();
var io = require('socket.io')(server);

io.on('connection',function(socket){
console.log('in socket');
t.on('tweet', function (tweet) {
    socket.emit('tweet',{"Username":tweet.user.screen_name,"Tweet":tweet.text});
});
 
t.on('error', function (err) {
  console.log('Oh no')
});

//t.track('modi');
});

server.listen(3000);








 



