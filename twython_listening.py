from twython import TwythonStreamer

APP_KEY='ABuoZU3ZvyKIQ5aGD8J6S50BY'
APP_SECRET='NFlmdkeuU8QkoHmQOufqncyDsKhdH85izRoklm7dQ0BUwoZGgo'
OAUTH_TOKEN='124088888-q1sVD5ylE7t2AgQJwqT8h2hQEyp89ZxYd5t8yr7t'
OAUTH_TOKEN_SECRET='8jIeYaPQqDt8QpnwajspyL4fnvX76zf5c89xjIzF1zvG2'


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')

    def on_error(self, status_code, data):
        print status_code

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()


stream = MyStreamer(APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
stream.statuses.filter(track='twitter')