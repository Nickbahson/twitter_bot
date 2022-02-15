IDEA:
----
  For better social media experience, like using your Twitter handles as customer care channels,
since it's easier for users to reach you via social media than via calls.

WORKFLOW:
--------
  The idea is to have the relevant departments responding to question(s) that are only related
to their department. Eg sales, repairs, a new product x, etc.

  Using an extra tool to manage such teams like; slack in this example, but one can switch to any. 
Customer queries (tweets) are forwarded to the right channels for the right response.

  One could also choose to automate some replies, like for repairs ask for location if it was not 
included in the tweets text, or ask clients not to share their sensitive details online, if their tweet texts include such.

    Better customer care experience, better reputation, better sales!!

REQUIREMENTS:
------------
* copy example.env as .env and follow below links on getting the right values for each.
* https://github.com/SlackAPI/python-slack-sdk#requirements
* https://docs.tweepy.org/en/v3.5.0/getting_started.html
* Run `pip install -r requirements.txt` to install the dependencies the app relies on.
* Then `python index.py` to start the app