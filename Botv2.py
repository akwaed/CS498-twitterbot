import tweepy
import time
from datetime import datetime
import openai
import logging

# Twitter API credentials
api_key  = "8FpCdvA1XvncJZBkkO9Rd97r8"
api_secret = "fxlDlkhMzDXedGpv8Epik7U1ve3GV55LfyxiL0TZtuAPMbsAJk"
access_token = "1551707928184455174-lKaMFMc25BKF6EQgV4ShOyzW99p0a9"
bearer_token= "AAAAAAAAAAAAAAAAAAAAAGJ%2BlgEAAAAAzJgRHRS2gkGH94y%2FNPTGMJt%2Bu2k%3DgtbzOergnPFjRpVvRNW61aH2UI07vvyDkdKNLUzmXboDXbjyJP"
access_token_secret = "hVVLuamRs9otYTYdmkpgZY3jHMdtGUCvpCecwNOrDK6jz"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Connecting to Twitter API
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Set up OpenAI API key
openai.api_key = "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"

# Define a function to generate a response from chatGPT
def generate_response(prompt):
    try:
        completions = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )

        message = completions.choices[0].text
        return message
    except requests.exceptions.RequestException as e:
        return "Error: failed to generate response from chatGPT. Please try again later."


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
                message= generate_response(tweet.text)
                logger.info("Replying {tweepy.User.username}")
                client.create_tweet(in_reply_to_tweet_id=tweet.id, text=message)
                start_id = tweet.id
            except Exception as error:
                print(error)

    # Delay (so the bot doesn't search for new tweets a bucn of time each second)
    time.sleep(5)
