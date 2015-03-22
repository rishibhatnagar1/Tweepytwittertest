''' Code by Rishi Gaurav Bhatnagar, because he is lazy and he likes to tweet, FAST'''
#!/usr/bin/env python2.7

import tweepy
import sys

htag = raw_input("Enter hastags: ")

#print(len(htag))
# Consumer keys and access tokens, used for OAuth
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

def tweetNow():
	tweet_text = raw_input("You tweet here hastag already added: ")
	if len(tweet_text) <= 140-len(htag):
    		api.update_status(status=tweet_text +" "+htag+" .")
	else:
    		print "tweet not sent. Too long. 140 chars Max."


while True:
	tweetNow()
