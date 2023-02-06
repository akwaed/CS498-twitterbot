#!/usr/bin/env python
# tweepy-bots/bots/autoreply.py

import tweepy
import logging
import datetime
import json
#from twibot import create_api
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

auth = tweepy.OAuth1UserHandler(
    "hRxPLfji4d3gh4U8ACY7cevlw", "9irTEkc9UAmDqD7mAIIGHpreNboOuOq0fJhKggXppCdom2HqNw",
     "1551707928184455174-3mGdfWvSJKINp00CxxswmIXvDL8Uyd", "XdXe89xJbKsIFZxRebSTJC86bEchzcmEZhLUfyKWVEp9M"
)
api = tweepy.API(auth)

# For the account name
def wipe(account_name="AElnoel", favorite_threshold=0, days=100):
    # Get the current datetime
    current_date = datetime.utcnow()

    # For each tweet
    for status in tweepy.Cursor(api.user_timeline, screen_name='@'+account_name).items():
        # Get the tweet id
        status_id = status._json['id']

        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'Examining', status_id)

        # Get the number of favorites
        api.destroy_status(status_id)
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'Deleting', status_id)
        

# Run main function
if __name__ == '__main__':
    wipe(account_name='AElnoel', favorite_threshold=0, days=100)

# def check_mentions(api, keywords, since_id):
#     logger.info("Retrieving mentions")
#     new_since_id = since_id
#     for tweet in tweepy.Cursor(api.mentions_timeline,
#         since_id=since_id).items():
#         print(tweet.text)
#         new_since_id = max(tweet.id, new_since_id)
#         if tweet.in_reply_to_status_id is not None:
#             continue
#         if any(keyword in tweet.text.lower() for keyword in keywords):
#             logger.info(f"Answering to {tweet.user.name}")

#             # if not tweet.user.following:
#             #     tweet.user.follow()

#             api.update_status(
#                 status="Please reach us via DMk",
#                 in_reply_to_status_id=tweet.id,
#             )
#     return new_since_id

# def main():
#     #api = create_api()
#     since_id = 1
#     while True:
#         since_id = check_mentions(api, ["help", "support"], since_id)
#         logger.info("Waiting...")
#         time.sleep(60)

# if __name__ == "__main__":
#     main()