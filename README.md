# twatterScripts
Various scripts using tweepy python module for interacting with the twitter API

Must have Python (duh!) - Must have tweepy module for python.

twatterFollowerScraper.py: This script will prompt you for a Twitter users screen name... for example my twitter account is @CowAnon so you would enter CowAnon and let the script do its work. It will create a file called CowAnon.txt, in the same directory, containing the twitter urls of all the accounts following me.

twatterSearch.py: This script still needs work... But at the moment it kinda works... You give it a search term and it will query twitters REST API for tweets containing that term. Results are saved to a file in json format and are saved into the same directory with the naming convention "Your Search Term.txt"

You will need to create your OWN twitter app (apps.twitter.com) and enter the appropriate Consumer/Access Keys & Secrets in the script - it is OBVIOUS where to enter this information..

Do not be alarmed if a script displays a message about the "rate limit". I assume that this is Twitters way of stopping us hammering its servers as we're pulling information from the API. The script will simply rest for 15 minutes until the next window is clear and will resume its work. This is nothing I can do anything about... Blame Twitter.

Thanks. 
#opISIS #opIceISIS
meowCow/m00cat/CowAnon
