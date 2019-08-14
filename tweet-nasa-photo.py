import sys
import requests
import tweepy
import shutil

# Consumer keys and access tokens, used for OAuth
consumer_key = os.getenv("consumer_key")
consumer_secret =  os.getenv("consumer_secret")
access_token = ''
access_token_secret = ''
nasa_key = ''
nasa_api = f"https://api.nasa.gov/planetary/apod?api_key={nasa_key}"
photo_filename = 'nasa_apod.jpg'
tweet_message = 'NASA Astrono ✨'


# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Call NASA API
r = requests.get(url = nasa_api)
data = r.json()
photo_url = data['url']

# Download file
response = requests.get(photo_url, stream=True)
with open('nasa_apod.jpg', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response

filenames = [photo_filename] # 
media_ids = []
for filename in filenames:
     res = api.media_upload(filename)
     media_ids.append(res.media_id)

# tweet with multiple images
api.update_status(status=tweet_message, media_ids=media_ids)
