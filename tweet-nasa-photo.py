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
media_filename = os.getenv("PHOTO_FILENAME")
tweet_message = ' ✨ Tweeting the NASA Astronomy Picture of the Day from an example Python script. @TwitterDev #TapIntoTwitter ✨'

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

media_url = data['url']
media_title = data['title'] #Do videos have titles? Assume so ;)
#media_description = data['explanation'] #Typically more than 280 characters. TODO: Build a mini-Tweet storm.

#Update tweet_message with this metadata
tweet_message = f"{media_title} \n \n {tweet_message}"

#Inspect URL and determine whether will need to download a photo file so we can natively Tweet it, OR
# If it is a video, then just post a link to the video hosted elsewhere...
native_media = False
if media_url.endswith('jpg') or media_url.endswith('png'):
    
    native_media = True
    # Download file
    print ('Downloading the NASA media...')
    response = requests.get(media_url, stream=True)
    with open(media_filename, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

    filenames = [media_filename] 
    media_ids = []
    for filename in filenames:
        res = api.media_upload(filename)
        media_ids.append(res.media_id)
else:
    native_media = False
    tweet_message = "It's time for a video! " + tweet_message + f"{media_url}"

if native_media:
    print ('Posting Tweet with media...')
    api.update_status(status=tweet_message, media_ids=media_ids)
else:
    tweet_text = tweet_message + " It's movie time... "
    print ('Pain old Tweet with an URL in message...')
    api.update_status(status=tweet_message)


