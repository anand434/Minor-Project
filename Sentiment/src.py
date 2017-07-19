import csv
import sys
import tweepy
from textblob import TextBlob

consumer_key = 'consumer key'
consumer_secret = 'consumer secret' 

access_token = 'access_token'
access_token_secret = 'access token secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

word = str(input("Enter the word to collect analysis : "))
public_tweets = api.search(word)

for tweet in public_tweets:
    print(tweet.text)
    # analysing tweets by tokenizing them
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
