#!/usr/bin/env python3
#
# This is a VERY simple non-elegant Python script to scrape a Twitter Accounts
# followers.
# You'll need your OWN twitter OAuth keys.... login to http://apps.twitter.com
# to set this up.... ALSO you'll need to install the python tweepy module..
# because we are using the tweepy module to interact with the twitter API
#
# 
#
# A couple of caveats: Twitters API throttles certain requests... So, when using
# this script on a user with lots of followers you WILL hit the "rate limit"
# at this point the script will stop and wait 15 minutes for the next "window"
# Please DO NOT quit the script.. just let it do it's thing... it WILL resume
# and continue scraping.
#
#
#

import time
import tweepy

consumer_key ='turyg3mVmnkXi2YDcYLRUUGLm'
consumer_secret='CMbOA6zauAsaF5H4TCg8TWX54dejumsK2Aw9IZDGAKqAbmN68V'
access_token='4867989411-1LyFLBrxUxBKEdE7Mx9Kk6qFgMdprO0CRy9RcIi'
access_secret='aEIU3qjlNBOYUqfG83bIqswAIvDhJPc4tebXNgpnhZXnf'
 
auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
if (not api):
     print('no login bitch')
     quit()

userINP = input ('Enter the Twitter screen name: ')


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
            u = next(user, False)
            list.write('twitter.com/{}\n'.format(u.screen_name))
            print ('Scraped user #{}'.format(x))
            print ('Follower twitter.com/{}'.format(u.screen_name))
            x+=1
        except KeyboardInterrupt:
            print ('  <--- You pressed Ctrl-C - Program terminated. Incomplete list written to file')
            quit()
        except tweepy.error.TweepError:
            print ('Houston, We have a problem! We may have reached the Twatter API rate limit')
            print ('If you get this right away - you can't scrape this user- Try another! \n')
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
