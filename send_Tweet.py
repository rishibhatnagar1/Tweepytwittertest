import tweepy

CONSUMER_KEY ="nZNaBHqEUFIVNeFBUUjFQWa3c"
CONSUMER_SECRET = "ltjmhAUnl6xbQa8ZzSW7XkM0heciSoO5YDMoGVjfpaw6nPoENe"   
ACCESS_KEY = "124088888-9bFnLQjsZTeGyKiZqYHyQ05ZsJkG9eaD4CywRd08"    
ACCESS_SECRET = "FXmtMaItnfXvFx5ybO8L6SIwO95TV58dhLmnTxAy01LfN"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)
api.update_status("Late-night #hack sessions should not start without #maggie")
print "tweeted"
