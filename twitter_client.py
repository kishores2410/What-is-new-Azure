
import os
import tweepy
from config import consumer_key, consumer_secret, access_token, access_token_secret

# Twitter API authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API client
client = tweepy.Client(bearer_token=os.getenv('TWITTER_BEARER_TOKEN'),
                       consumer_key=consumer_key, 
                       consumer_secret=consumer_secret,
                       access_token=access_token,
                       access_token_secret=access_token_secret)