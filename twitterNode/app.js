var config = require('./config.json');
var express = require('express');
var app = express();

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
app.setHeaders(header);

/* Express serving static file */
var path = require('/path');
app.use('/static',express.static(path.join(__dirname+'/public')));


/**    GET function which takes a route on which the call needs to act and also the File to return
 **/
 getfile: function(onPath, returnFileFunc) {
	  app.get(onPath, function(req, res) {
            try {
                if (typeof returnFileFunc == 'function') {
                    res.sendFile(path.join(__dirname, '../../', returnFileFunc(false, req.query)));
                } else {
                    res.sendFile(path.join(__dirname, '../../', returnFileFunc))
                }
            } 
		catch (e) {
                if (typeof returnFileFunc == 'function') {
                    returnFileFunc(e, "");
                } 
		else {
                    throw e;
                }
            }
        });
}

app.getfile('/', function (err, query) { 
	if (!err) {
		return "./index.html"; 
	} 
	else { 
		console.log(err); 
		return err; 
	} 
})

app.get('/tweet', function (err, query) {
        if (!err) {
                t.track(query.search);
                return "done";
        }
        else {
                console.log(err);
                return err;
        }
});


var server = app.getSocketServer();
var io = require('socket.io')(server);

io.on('connection',function(socket){
console.log('in socket');
t.on('tweet', function (tweet) {
    socket.emit('tweet',{"Username":tweet.user.screen_name,"Tweet":tweet.text});
	
});
 
t.on('error', function (err) {
  console.log('Oh no')
});

t.track('pussy');
});

server.listen(3000);








 



