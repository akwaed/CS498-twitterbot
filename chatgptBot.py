#!/usr/bin/env python
# tweepy-bots/bots/autoreply.py

import tweepy
import logging
#from twibot import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

auth = tweepy.OAuth1UserHandler(
    "xkoE1WFTIxzudZZmfdEYX5lhZ", "wqme6fzwFdHz8HTrm0e15ca3K7V2eVexMePQ3px9t7L2a0Mw7w",
     "1551707928184455174-vsyC8C4rE1vA058igsQXAW2SU3B28E", "egxhRJojKFRDF9zIH6wBtLA7bW3ts2qlL7ZR69zCSWIxj"
)
api = tweepy.API(auth)

def check_mentions(api, keywords, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():
        print(tweet)
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            logger.info(f"Answering to {tweet.user.name}")

            if not tweet.user.following:
                tweet.user.follow()

            api.update_status(
                status="Please reach us via DM",
                in_reply_to_status_id=tweet.id,
            )
    return new_since_id

def main():
    #api = create_api()
    since_id = 1
    while True:
        since_id = check_mentions(api, ["help", "support"], since_id)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()