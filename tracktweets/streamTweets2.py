#Import modules and stuff for tracking
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import configV
import time
import json
from HTMLParser import HTMLParser
################### Keys ##################
ckey =configV.values["ckey"] 
csecret =configV.values["csec"]
atoken = configV.values["otoken"]
asecret = configV.values["osec"]

class listener(StreamListener):

    def on_data(self, data):
        try:
		#print data
		''' convert data into json '''
		data = json.loads(HTMLParser().unescape(data))	
		#tweet = data['text']
		namee = data["user"]["screen_name"]
		print namee
		return True
	except BaseException, e:
		print 'failed on data',str(e)
    		time.sleep(2)
	def on_error(self, status):
       		 print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=[""])

