#Twitter Streaming with Python

In the codes, you will find 3, pullHastags , streamTweets1 and 2. 
```
pullHastags uses on_data method from tweepy and is a little painful because I am splitting the data input instead of using is like a json formatted structure.
streamTweets1 use on_status method from tweepy, is super easy to use and gives you the ouput in the form "blah blah blah"-NameOfPerson . I have added a few more details to the data,location, number of followers of the person, and a few other things.
streamTweet2 uses on_data itslef but the data is converted to json using HTML parser and json as inputs. 
```
I have used configV as a module, this stores my tokens. You don't need to do this. What you can simply do is in the consumerkey,secret etc field, copy the values from app.twitter.com and you are done. I just wanted to keep my data safe. Planning to intergrate it for a db which could be used for later uses. Might intergrate it with pygame, just because I like to experiment with multiple things at the same time. Let's see if I get the time.
 For any doubts, recommendations, just write to me. Peace!
