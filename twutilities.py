import oauth2
import json
from tweepy import OAuthHandler

# Variables that contains the user credentials to access Twitter API
access_token = "your at"
access_token_secret = "your ats"
CONSUMER_KEY = "your ck"
CONSUMER_SECRET = "your cs"

# OAuth
def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth2.Token(key=access_token, secret=access_token_secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content

# Fetch the user's timeline data (includes info about them)
def getTimeline(sname, numtweets):

    if not numtweets:
        numtweets = 20

    # Twitter API will return a set of tweets in JSON format
    user_timeline = oauth_req( 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=%s&count=%s&tweet_mode=extended' % (sname, numtweets), CONSUMER_KEY, CONSUMER_SECRET )

    # returns the timeline of JSON-formatted tweets
    return user_timeline

# Grab and display the data about this user account
def getUserData(timeline):

    if timeline != "":
        # convert JSON array into a dict of a single tweet, cuz we just want the USER data
        userdict = json.loads(timeline)[0]

        # Then build an output string called usercard that we can return
        if userdict["user"]["time_zone"]:
            usercard = "\nThis account's time zone is set to %s" % userdict["user"]["time_zone"].encode('ascii','replace')
        else:
            usercard = "This account has not set their time zone."
        usercard += "\nThey say their location is %s" % userdict["user"]["location"].encode('ascii','replace')
        usercard += "\nTheir account was created at %s" % userdict["user"]["created_at"].encode('ascii','replace')
        if userdict["user"]["default_profile_image"]:
            usercard += "\n\nThey might be an egg!"
        else:
            usercard += "\n\nThey've changed their profile image; no longer an egg."
        usercard += "\nThey have contributors set to (rarely T): %s" % userdict["user"]["contributors_enabled"]
        if userdict["user"]["verified"]:
            usercard += "\nThey're verified -- probably legit!"
        else:
            usercard += "\nThey are not verified."
        usercard += "\n\nThey've tweeted %s times" % userdict["user"]["statuses_count"]
        usercard += "\nThey have %s followers" % userdict["user"]["followers_count"]
        usercard += "\nThey have %s friends" % userdict["user"]["friends_count"]

        # name is a tuple
        usercard += "\n\nTheir name is %s" % str(userdict["user"]["name"].encode('ascii','replace'))
        usercard += "\nTheir description is:\n"
        usercard += userdict["user"]["description"].encode('ascii','replace')

        # Return a string-formatted output of their user info
        return usercard
    else:
        return "Not a found Twitter user."

# Just print out all this user's tweets that we have
def printUserTweets(timeline):
    # creates a list of dicts
    tweetslist = json.loads(timeline)

    for tweet in tweetslist:
        print(tweet["full_text"])

# Return a List all this user's tweets that we have
def returnUserTweets(timeline):
    # creates a list of dicts
    tweetslist = json.loads(timeline)
    usertweets = []

    for tweet in tweetslist:
        usertweets.append(tweet["full_text"])

    return usertweets
