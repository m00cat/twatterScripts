# twatterScripts
Various scripts using tweepy python module for interacting with the twitter API

Must have Python (duh!) - Must have tweepy module for python.

At the moment I only have the ONE script. This script will prompt you for a Twitter users screen name... for example my twitter account is @CowAnon so you would enter CowAnon and let the script do its work. It will create a file called CowAnon.txt containing the twitter urls of all the accounts following/followed by me.

You will need to create your OWN twitter app (apps.twitter.com) and enter the appropriate Consumer/Access Keys & Secrets in the script - it is OBVIOUS where to enter this information..

Do not be alarmed when the script stops saying it has run into the rate limit problem.. this is Twitters way of stopping us hammering its servers pulling information from the API. The script will simply rest for 15 minutes until the next window is clear and will resume scraping. This is nothing I can do anything about... Blame Twitter.

Thanks. #opISIS
meowCow/m00cat/CowAnon
