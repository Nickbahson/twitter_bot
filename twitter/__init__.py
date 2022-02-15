import os
import time

import tweepy

import models
from slack import sendItem

consumer_key = os.environ["TWITTER_API_KEY"]
consumer_secret = os.environ["TWITTER_API_KEY_SECRET"]
access_token = os.environ["TWITTER_ACCESS_TOKEN"]
access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]


class StreamListener(tweepy.Stream):
    def on_status(self, status):
        name = models.channel_name(status.text)
        sendItem(name, "A title", status.text)

    def on_connection_error(self):
        self.disconnect()

    def on_limit(self, status):
        print("Rate Limit Exceeded, Sleep for 15 Mins")
        time.sleep(15 * 60)
        return True


tweeterSteamListener = StreamListener(
    consumer_key, consumer_secret,
    access_token, access_token_secret,
    max_retries=20
)
