var app= require('express')();
var server =require('http').Server(app);
var io = require('socket.io')(server);
server.listen(3000);

var lastImage = ''; 
var Twit = require('twit'),
config = require('./config');

app.get('/', function (req, res) {
  res.sendfile(__dirname + '/index.html');
});
var T = new Twit(config.auth);
var initStream = function(user_ids) {
    // Start listening to stream
    var stream = T.stream('statuses/filter', {track: config.hashtags.join()});
    io.on('connection',function(socket){
        console.log("In socket");    
        stream.on('tweet', function(tweet) {
            var images = [];
            if ('media' in tweet.entities) {
                images = tweet.entities.media.filter(function(media) {
                    return media.type == 'photo';
                }).map(function(media) {
                    return media.media_url;
                });
            } else if ('urls' in tweet.entities) {
                images = tweet.entities.urls.filter(function(url) {
                    return url.expanded_url.indexOf('instagr') != -1;
                }).map(function(url) {
                    return url.expanded_url + 'media?size=l';
                });
            }
            if (images.length > 0) {
                lastImage = images[0];
                
                //eventEmitter.emit('newImage');
                socket.emit('tweet',{"Username":tweet.user.screen_name,"Tweet":tweet.text,"imageLink":tweet.user.profile_image_url,"retweets":tweet.retweet_count,"mediaLink":lastImage});
                }
                console.log('New image: ' + lastImage);
            
        });

    });
}

// initialize Twitter stream without users
initStream([]);