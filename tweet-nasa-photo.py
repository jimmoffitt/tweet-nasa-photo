import sys
import requests
import tweepy
import shutil
import os
from dotenv import load_dotenv
load_dotenv(verbose=True)  # Throws error if it can't find .env file

print ("Retrieving credentials...")
# Twitter API details. Consumer keys and access tokens, used for OAuth.
consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret =  os.getenv("TWITTER_CONSUMER_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# NASA API details
nasa_key = os.getenv("NASA_KEY")
nasa_api = os.getenv("NASA_API")
nasa_url = f"{nasa_api}?api_key={nasa_key}"

#Bot details
photo_filename = os.getenv("PHOTO_FILENAME")
tweet_message = ' ✨ NASA Astronomy Picture of the Day from an example Python script.  #TapIntoTwitter ✨'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Call NASA API
print ('Calling the NASA API and retrieving photo metadata...')
r = requests.get(url = nasa_url)
data = r.json()
#print (data)

photo_url = data['url']
photo_title = data['title']
#photo_description = data['explanation'] #Typically more than 280 characters.
#Update tweet_message with this metadata
tweet_message = f"{photo_title} \n \n {tweet_message}"

# Download file
print ('Downloading the NASA media...')
response = requests.get(photo_url, stream=True)
with open(photo_filename, 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response

filenames = [photo_filename] 
media_ids = []
for filename in filenames:
     res = api.media_upload(filename)
     media_ids.append(res.media_id)

# tweet with multiple images
print ('Posting Tweet with media...')
api.update_status(status=tweet_message, media_ids=media_ids)

