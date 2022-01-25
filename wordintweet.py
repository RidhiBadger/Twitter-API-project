import twitter
import json
import argparse
import spacy
import re
#from datetime import datetime
import time
import requests
import base64
import numpy as np
import warnings
import os
import tweepy as tw
import pandas as pd

##api = twitter.Api(consumer_key = '****', consumer_secret = '****', access_token_key = '****', access_token_secret = '****')


consumer_key = '****'
consumer_secret = '****'
access_token = '****'
access_token_secret = '****'



auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth)

search_words = "#life"
date_since = "2022-01-01"
tweets = tw.Cursor(api.search_tweets,
              q=search_words,
              lang="en",
              since=date_since).items(10)

for tweet in tweets:
    print(tweet.text)

