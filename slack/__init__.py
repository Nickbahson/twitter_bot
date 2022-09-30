import os
from slack_sdk.webhook import WebhookClient

#client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])


# def sendItem(channel, title, message):
#     res = client.chat_postMessage(channel=channel, text=message)
#     if res.status_code != 200:
#         raise Exception(res.status_code, res)

def webhook_request(channel, title, tweet):
    url = os.environ['SLACK_WEBHOOK_URL']
    webhook = WebhookClient(url)

    tweet_url = "https://twitter.com/twitter/statuses/{}".format(tweet.id)
    message = "You have a new request:" \
              "\n*<{}|Newest - tweet>*" \
              "\n*Tweet body:* {} ." \
              "\n*For channel:* {} ".format(tweet_url, tweet.text, channel)

    # Free api, sends to #general channel
    r = webhook.send(text=title, blocks=[
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": message
            }
        }
    ])
    if r.status_code != 200:
        raise Exception(r.status_code, r)