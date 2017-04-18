# -*- coding: utf-8 -*-
import tweepy, time, sys

argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
consumer_key = 'abcd'#keep the quotes, replace this with your consumer key
consumer_secret = 'abcd'#keep the quotes, replace this with your consumer secret key
access_key = 'abcd'#keep the quotes, replace this with your access token
access_secret = 'abcd'#keep the quotes, replace this with your access token secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(status=line)
    time.sleep(200) #change this depending on the time interval you want to tweet
