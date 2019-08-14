# Tweet Nasa Photo

A super simple code that Tweets a photo downloaded from the NASA APOD API. 

https://apod.nasa.gov/apod/astropix.html


## Running the script.

+ Clone the repository.
+ Create a .env file and fill in your private credentials. .env.example is provided as a template.
+ Update the Tweet message at the top of the tweet-nasa=photo.py code. 
+ Execute the script: c>python3 tweet-nasa-photo.py 
+ Go admire the NASA Astronomy Photo of the Day on your Timeline. 

## Dependencies
- Python (recommended >= 3.6 for f-string support)
- Tweepy - Python wrapper for Twitter APIs
  - Provides methods for:
    - Uploading media to Twitter in 'chunks'
    - Post Tweets with media. 
    

```python
import sys
import requests
import tweepy
import shutil
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

