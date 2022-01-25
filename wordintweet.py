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


consumer_key = 'N3tyUxK9u2QKCkA1p1Gw5eDJd'
consumer_secret = 'MCk9sLTGhtE4Za1fRO6ruHCy0h4TdicseVsv3eyFF5gy7qRNs1'
access_token = '165846689-sj7w4uhLzK7UMTK11xhmxWBRPbfGCzxm05vQ9q3S'
access_token_secret = 'SVageJRbtIqpKmXctbLHhrBYxJm8TDe7q9EPL4EZBkhWj'



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

