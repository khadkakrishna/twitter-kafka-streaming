from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer
import json
import twitter_configurations

#TWITTER API CONFIGURATIONS
consumer_key = twitter_configurations.consumer_key
consumer_secret = twitter_configurations.consumer_secret
access_token_key = twitter_configurations.access_token_key
access_token_secret = twitter_configurations.access_token_secret

hashtags=['covid', 'covid19']

class StdOutListener(StreamListener):
    def on_data(self, data):
        json_ = json.loads(data) 
        producer.send("twitter-topic", json_["text"].encode('utf-8'))
        return True
    def on_error(self, status):
        print (status)

producer = KafkaProducer(bootstrap_servers='localhost:9092')
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
stream = Stream(auth, l)
stream.filter(track=hashtags)
