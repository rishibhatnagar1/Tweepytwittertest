#Import modules and stuff for tracking
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import configV



################### Keys ##################
ckey =configV.values["ckey"] 
csecret =configV.values["csec"]
atoken = configV.values["otoken"]
asecret = configV.values["osec"]

class listener(StreamListener):

    def on_data(self, data):
        print data["text"]
        return True

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])





