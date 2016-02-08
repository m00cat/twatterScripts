#!/usr/bin/env python3
#
# This is a VERY simple non-elegant Python script to scrape a Twitter Accounts
# followers! Could EASILY be modified to scrape those _following_ the account.
# You'll need your OWN twitter OAuth keys.... login to http://apps.twitter.com
# to set this up.... ALSO you'll need to install the python tweepy module..
# because we are using the tweepy module to interact with the twitter API
# So.. from a command prompt do: pip3 install tweepy 
#
# As far as I know tweepy only works on python3 
# 
#
# A couple of caveats: Twitters API throttles certain requests... So, when using
# this script on a user with lots of followers you WILL hit the "rate limit"
# at this point the script will stop and wait 15 minutes for the next "window"
# Please DO NOT quit the script.. just let it do it's thing... it WILL resume
# and continue scraping. If you can run the script on Googles App Engine
# You can comment out the section relating to the the rate limit as there IS
# no rate limit when running on their servers.. however you may start using a lot
# of CPU cycles on your APP engine account and end up getting charged.. it's up to
# you... make the decision yourself.
#
#
#


import time
import tweepy

# insert your Twitter keys here
consumer_key ='Your_Consumer_Key'
consumer_secret='Your_Consumer_Secret'
access_token='Your_Access_Token'
access_secret='Your_Access_Secret'

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

userINP=input( "Enter the Twitter screen name : " )


#This writes a file named 'USERNAME_YOU_ENTERED.txt' to the same directory you
# have the script in - you can give it a path, if you like!
with open('{}.txt'.format(userINP),'w') as list:
 
    # Login
    if(api.verify_credentials):
        print ('We are logged in!')
 
    user = tweepy.Cursor(api.followers, screen_name=userINP).items()
    x=1
    while True:
        try:
            print ('Scraping.... ')
            u = next(user, False)
            list.write('twitter.com/{}\n'.format(u.screen_name))
            print ('Scraped twitter.com/{}'.format(u.screen_name))
            print ('Added to list DaeshBAG Number: {}\n'.format(x))
            x+=1
            #time.sleep(2*1)
        except KeyboardInterrupt:
            print ('  <--- You pressed Ctrl-C - Program terminated. File not written to disk!')
            break
        except tweepy.error.TweepError:
            print ('Houston, We have a problem! We may have reached the Twatter API rate limit')
            print ('We are now forced to wait 15 minutes for next window.. Blame Twatter! \n')
            time.sleep(15*60)
            #continue
        except:
            if u is False:
                print ('Done! Now pastebin the contents of the list in this directory!')
                print ('Post the pastebin url in #opISIS-Targets')
                print ('for addition to the botnet...')
                print ('Have a coffee and do it again!')
                print ('Don\'t run the script too many times consecutively')
                print ('or you\'ll run into rate limit problems.. 4 or 5 times an hour!') 
                quit()
