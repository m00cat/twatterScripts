#!/usr/bin/env python3
#
# needs tweepy & jsonpickle 
# when given a search term will return a 
# json formatted list of tweets containing the term
# along with all relevant user info
#

import tweepy
# Replace the API_KEY and API_SECRET with your application's key and secret.
mykey ='API_KEY'
mysecret='API_SECRET'
print ("Authenticating")
auth = tweepy.AppAuthHandler(mykey, mysecret)
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
if (not api):
        print ("Can't Authenticate")
        sys.exit(-1)


import sys
import jsonpickle
import os
import json
searchQuery = input ('Enter the search term: ') # this is what we're searching for
maxTweets = 10000000 # Some arbitrary large number
tweetsPerQry = 100  # this is the max the API permits
fName = '{}.txt'.format(searchQuery) # We'll store the tweets in a text file.


# If results from a specific ID onwards are reqd, set since_id to that ID.
# else default to no lower limit, go as far back as API allows
sinceId = None

# If results only below a specific ID are, set max_id to that ID.
max_id = -999999999999999999999999999999999999

tweetCount = 0
print("Downloading max {0} tweets".format(maxTweets))
with open(fName, 'w') as f:
    while tweetCount < maxTweets:
        try:
            if (max_id <= 0):
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry)
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            since_id=sinceId)
            else:
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1))
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1),
                                            since_id=sinceId)
            if not new_tweets:
                print("No more tweets found")
                break
        
            for tweet in new_tweets:
               pickled = jsonpickle.encode(tweet._json, unpicklable=False)
               f.write(json.dumps(json.loads(pickled), indent=4, sort_keys=True))
            tweetCount += len(new_tweets)
            print("Downloaded {0} tweets".format(tweetCount))
            max_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            # Just exit if any error
            print("something went wrong. Error : " + str(e))
            break

print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))

 
