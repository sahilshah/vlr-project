from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="uT183BEs2QfZFZxAbQ3bKrBO0"
consumer_secret="TQVqtAzkxNf9RtFbSKOngs9iUcOFTB8ebMWQnBRqJP3HP6UpOA"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="31341259-bzwZny7Mo99JR28S4iSArDwZEpKRURaAvRXGm7I60"
access_token_secret="0NJOMzZU9bUvcoWY3hpCg811u5zZz4Z6HG7Yt4SiigwIx"

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """

    def on_data(self, data):
        decoded = json.loads(data)
        print(decoded['text'])
        try: 
            print(decoded['entities']['media'][0]['media_url'])
        except KeyError:
            print("No media")
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['#basketball'])