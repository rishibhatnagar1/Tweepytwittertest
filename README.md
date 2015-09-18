All the hacks I keep experimenting with have been put up here, more integrations are on its way. 
Next one, embed images with the tweets.

Update 09/18/15:
I have written 2 codes for streaming tweets. One called "streamingAPI" used the twitter-node-lib. It is rather easy to use. The only problem being, I was not able to separate the images in the entities. On doing a search of image_url in the twitter.entities.media , I get the value undefined.

The above problem apparently arised because the lib I used is based on twitter streaming API and does not have "endpoints" that I need to retrieve the images. I am still not sure what that means though.

The other node script I have written uses Twit which is both streaming REST capable. That to this wonderful hacker who wrote an implementation of this: https://github.com/visionect/twitterstreamer . Loved it, super easy to use. I dumbed it down for my own purposes and I have written the script for it. More updates soon.


Tracking tweets also working. Code tested
