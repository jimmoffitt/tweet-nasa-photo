import sys
import requests
import tweepy
import shutil
import os
from dotenv import load_dotenv
load_dotenv(verbose=True)  # Throws error if it can't find .env file

# Twitter API details. Consumer keys and access tokens, used for OAuth.
consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret =  os.getenv("TWITTER_CONSUMER_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# NASA API details
nasa_key = os.getenv("NASA_KEY")
nasa_api = os.getenv("NASA_API")
nasa_url = f"{nasa_api}?api_key={nasa_key}"
print (nasa_url)

#Bot details
photo_filename = os.getenv("PHOTO_FILENAME")

#Change this to make your Tweets more interesting...
tweet_message = ' ✨ NASA Astronomy Picture of the Day from a 40-line Python script. #TapIntoTwitter ✨'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Call NASA API
print ("Calling the NASA API")
r = requests.get(url = nasa_url)
data = r.json()
print (data)

#Extract response metadata for downloading media and including in Tweet message. 
photo_url = data['url']

# Download file
print ("Downloading a single NASA photo...")
response = requests.get(photo_url, stream=True)
with open(photo_filename, 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response

#Prepare post metdata, not that this script only handles a single photo. 
filenames = [photo_filename] # 
media_ids = []
for filename in filenames:
     res = api.media_upload(filename)
     media_ids.append(res.media_id)

# tweet with multiple images
print (f"Tweeting: {tweet_message}"
api.update_status(status=tweet_message, media_ids=media_ids)
