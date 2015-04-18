#Import modules and stuff for tracking
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import configV #My tokens stored here , you can replace them with your token below directly
import time
################### Keys ##################
ckey =configV.values["ckey"] 
csecret =configV.values["csec"]
atoken = configV.values["otoken"]
asecret = configV.values["osec"]

class listener(StreamListener):
	''' On status worked better than on_data. The json format can be directly used here '''
	def on_status(self, status):
		try:
			tweet = '"'+status.text+'"'+ status.user.screen_name
			print tweet
			''' you can get more details from the tweets here '''
			print "From Location: ",status.user.location
			print "Total Tweets: ",status.user.statuses_count
			print "friends: ",status.user.friends_count
			print "followers: ",status.user.followers_count
			print "favourites: ",status.user.favourites_count
			print "Created at: ",status.user.created_at
			print '\n'
		except BaseException, e: #Called on any exception
			print 'failed on data',str(e)
    			time.sleep(2)
	
	on_event = on_status
	
	def on_error(self, status):
		print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
''' Enter the string that needs to be tracked '''
twitterStream.filter(track=[""])

