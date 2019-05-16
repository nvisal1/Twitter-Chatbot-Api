import tweepy 		#https://github.com/tweepy/tweepy
import sys
import csv
import re
import os
import json

# Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

def get_all_tweets(query):	
	#--- authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	#--- get tweets 
	alltweets = []
	alltweets.extend(tweepy.Cursor(api.search, q=query, rpp=10, result_type="recent", include_entities=True, lang="en").items(10))

	return alltweets

def creds():
  global consumer_key, consumer_secret, access_key, access_secret

  dir_path = os.path.dirname(os.path.realpath(__file__))

  with open(dir_path + '/creds.json', 'r') as f:
    credentials = json.load(f)

    consumer_key = credentials['consumer_key']
    consumer_secret = credentials['consumer_secret']
    access_key = credentials['access_key']
    access_secret = credentials['access_secret']

creds()

