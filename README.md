# Tweet NASA Photo

A super simple Python script that Tweets a photo downloaded from the NASA APOD API. 

https://apod.nasa.gov/apod/astropix.html

## Get access to APIs:

+ Get a Twitter Developer account, create and a Twitter app and reference the "consumer" tokens: https://developer.twitter.com/en/account/get-started
+ Start here and get your NASA API Key: https://api.nasa.gov/

## Running the script.
This script was put together without support for command-line arguments. 

+ Clone the repository. 
+ Run `pip install requirements.txt` to install the third-party library dependenices.
+ Create a .env file and fill in your private credentials. .env.example is provided as a template.
+ Update the Tweet message at the top of the tweet-nasa-photo.py code. 
+ Execute the script: c>python3 tweet-nasa-photo.py 
+ Go admire the NASA Astronomy Photo of the Day on your Timeline. 

## Dependencies
- Python (recommended >= 3.6 for f-string support)
- Tweepy - Python wrapper for Twitter APIs
  - Provides methods for:
    - Uploading media to Twitter in 'chunks'.
    - Post Tweets with media. 
- .env configuration functionality based on `python-dotenv` package.
    

```python
import sys
import requests
import tweepy
import shutil
import os
from dotenv import load_dotenv #python-dotenv package.
```
  
  
## Configuration
Create a file named ".env" at the root of the repository directory with the relevant credentials (see '.env.example'). Here's the example '.env' for reference:

```
# Twitter app creds for app uploading and posting Tweets. 
TWITTER_CONSUMER_KEY=""
TWITTER_CONSUMER_SECRET=""
TWITTER_ACCESS_TOKEN=""
TWITTER_ACCESS_TOKEN_SECRET=""

#NASA API details
NASA_KEY=""
NASA_API="https://api.nasa.gov/planetary/apod"

#Bot details
PHOTO_FILENAME="current.jpg"
```

