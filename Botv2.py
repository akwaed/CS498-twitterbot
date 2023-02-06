import tweepy
import time
from datetime import datetime
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


# Twitter API credentials
api_key  = "8FpCdvA1XvncJZBkkO9Rd97r8"
api_secret = "fxlDlkhMzDXedGpv8Epik7U1ve3GV55LfyxiL0TZtuAPMbsAJk"
access_token = "1551707928184455174-lKaMFMc25BKF6EQgV4ShOyzW99p0a9"
bearer_token= "AAAAAAAAAAAAAAAAAAAAAGJ%2BlgEAAAAAzJgRHRS2gkGH94y%2FNPTGMJt%2Bu2k%3DgtbzOergnPFjRpVvRNW61aH2UI07vvyDkdKNLUzmXboDXbjyJP"
access_token_secret = "hVVLuamRs9otYTYdmkpgZY3jHMdtGUCvpCecwNOrDK6jz"

# Connecting to Twitter API
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Message to reply with if someone mentions the bot
message = "Our bot works Perfect, Team Twitter API is awsome"

# Bot's unique ID
client_id = client.get_me().data.id

# This is so the bot only looks for the most recent tweets.
start_id = 1
initialisation_resp = client.get_users_mentions(client_id)
if initialisation_resp.data != None:
    start_id = initialisation_resp.data[0].id

# Looking for mentions tweets in an endless loop
while True:
    logger.info("Retrieving mentions")
    response = client.get_users_mentions(client_id, since_id=start_id)

    # Reply Code
    if response.data != None:
        for tweet in response.data:
            try:
                print(tweet.text)
                logger.info(f"Answering to {tweet.user.name}")
                client.create_tweet(in_reply_to_tweet_id=tweet.id, text=message)
                start_id = tweet.id
            except Exception as error:
                print(error)

    # Delay (so the bot doesn't search for new tweets a bucn of time each second)
    time.sleep(5)