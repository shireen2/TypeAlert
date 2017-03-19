import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = 'oB8MprtdAXWkY781ik84UItPB'

consumer_secret = 'qvsEJsPWNWbCdbnrxZ5JU8nxBfXGZDMUAsHKB6gqccAClPQ48v'

access_token = '842985841228206080-JtJ4roKVnnENE2kmIG3WdsnlnSy9t6J'

access_secret = 'ennXsru7hg0jTzEdlzjN1OHqTQOpg8gMJYbhGJxmPpSka'

auth = OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

class listener(StreamListener):
    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print (status)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["trump"])
