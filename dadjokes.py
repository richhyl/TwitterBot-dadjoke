#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys, random
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = ''#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = ''#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = ''#keep the quotes, replace this with your access token
ACCESS_SECRET = ''#keep the quotes, replace this with your access token secret

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

followers = api.followers()

with open('text.txt') as f:
   lines = f.readlines()

while True:
	line = "@{} {} #dadjoke".format(random.choice(followers).screen_name, random.choice(lines).strip())
	api.update_status(status=line)
	print line 
	time.sleep(900)#Tweet every 15 minutes()
	sys.exit()