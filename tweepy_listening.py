from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener 

ckey ='ABuoZU3ZvyKIQ5aGD8J6S50BY'
csecret='	NFlmdkeuU8QkoHmQOufqncyDsKhdH85izRoklm7dQ0BUwoZGgo'
accesstoken ='124088888-q1sVD5ylE7t2AgQJwqT8h2hQEyp89ZxYd5t8yr7t'
accesssecret ='8jIeYaPQqDt8QpnwajspyL4fnvX76zf5c89xjIzF1zvG2'

class listener(StreamListener):
	"""docstring for StreamListener"""
	def on_data(self, data):
		#super StreamListner, self).__init__()
		#self.arg = arg
		print data
		return True

	def on_error(self,status):
		print status

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(accesstoken,accesssecret)
twitterStream = Stream(auth,listener())
twitterStream.filter(track =["car"])