import os
from slack_sdk import WebClient

client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])


def sendItem(channel, title, message):
    res = client.chat_postMessage(channel=channel, text=message)
    if res.status_code != 200:
        raise Exception(res.status_code, res)
