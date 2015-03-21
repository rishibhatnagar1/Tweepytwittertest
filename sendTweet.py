#!/usr/bin/env python2.7
  
import tweepy
import sys

htag1 = raw_input("Enter hastag 1")
'''
ques = raw_input("got more hastags? Y or N ?")
if (ques =="Y"):
	htag2 = raw_input("Enter hastag 2")
if (ques =="N"):

'''	
# Consumer keys and access tokens, used for OAuth
consumer_key = 'nZNaBHqEUFIVNeFBUUjFQWa3c'
consumer_secret = 'ltjmhAUnl6xbQa8ZzSW7XkM0heciSoO5YDMoGVjfpaw6nPoENe'
access_token = '124088888-9bFnLQjsZTeGyKiZqYHyQ05ZsJkG9eaD4CywRd08'
access_token_secret = 'FXmtMaItnfXvFx5ybO8L6SIwO95TV58dhLmnTxAy01LfN'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

def tweetNow():
	tweet_text = raw_input("You tweet here hastag already added: ")
	if len(tweet_text) <= 118:
    		api.update_status(status=tweet_text +""+htag1+" .")
	else:
    		print "tweet not sent. Too long. 140 chars Max."


while True:
	tweetNow()
