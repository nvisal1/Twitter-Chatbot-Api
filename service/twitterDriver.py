import tweepy 		#https://github.com/tweepy/tweepy
import sys
import csv
import re

#Twitter API credentials
# consumer_key = ""
# consumer_secret = ""
# access_key = ""
# access_secret = ""

def get_all_tweets(query):	
	#--- authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	#--- get tweets 
	alltweets = []
	alltweets.extend(tweepy.Cursor(api.search, q=query, rpp=10, result_type="recent", include_entities=True, lang="en").items(10))

	return alltweets;
