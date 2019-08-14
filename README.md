# Tweet Nasa Photo

A super simple code that Tweets a photo downloaded from the NASA APOD API. 



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
# Account creds for PowerTrack, Historical PowerTrack, and Search API
USERNAME=""
PASSWORD=""
ACCOUNT_NAME=""
POWERTRACK_LABEL=""
SEARCH_LABEL=""

# Twitter app creds for Engagement API
TWITTER_CONSUMER_KEY=""
TWITTER_CONSUMER_SECRET=""
TWITTER_ACCESS_TOKEN=""
TWITTER_ACCESS_TOKEN_SECRET=""
TWITTER_BEARER_TOKEN=""
```

Note: The Engagement-API/generate_bearer_token.py script can be used to generate a bearer token. You can then store that returned value in the '.env' file as shown above.
