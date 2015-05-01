#Import modules and stuff for tracking
import tweepy
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
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
rtcount = 0
def retweetNow(id):
	api.retweet
	rtcount+=1
	print "Total RTs: ",count
	
class listener(StreamListener):
	''' On status worked better than on_data. The json format can be directly used here '''
	def on_status(self, status):
		try:
			if (keyWord in status.text):
 			#and if(status.user.screen_name = "makewithWP" or status.user.screen_name ="anool"):
				print status.text
				print status.id
				#retweetNow(status.id)
				print '\n'
		except BaseException, e: #Called on any exception
			print 'failed on data',str(e)
    			time.sleep(2)
	
	on_event = on_status
	
	def on_error(self, status):
		print status
''' Wait for the input '''
__track = raw_input("Enter something you want to track: ")
keyWord = raq_input("Enter the keyWord for condition: ")
twitterStream = Stream(auth, listener())
''' Enter the string that needs to be tracked '''
twitterStream.filter(track=[__track])

