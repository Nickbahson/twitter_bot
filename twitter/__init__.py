import os
import time

import tweepy

import models
from slack import webhook_request # sendItem

consumer_key = os.environ["TWITTER_API_KEY"]
consumer_secret = os.environ["TWITTER_API_KEY_SECRET"]
access_token = os.environ["TWITTER_ACCESS_TOKEN"]
access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]


class StreamListener(tweepy.Stream):
    def on_status(self, status):
        # print('++++++++++ a new status ++++++++++++')
        # print(status)
        # print('++++++++++ a new status ++++++++++++')
        name = models.channel_name(status.text)

        # If tweet of interest if found, matching each
        # slack channel(department) or duties (responsibilities).

        # if  name == '#random':
        #     print(' +++ belongs to channel +++++')
        #     print(name)
        #     print(' +++ belongs to channel +++++')
        #     return
        # sendItem(name, "A title", status.text)
        webhook_request(name, "A new item was found", status)

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
