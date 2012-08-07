hitp_twitter_bot
================

A bot that retweets stuff for @HackersInThePub

Setup
-----

Create an application at https://dev.twitter.com/apps.

1. Set the following variables to the correct values from you app and twitter user that should do the retweeting: 

    CONSUMER_KEY = u''

    CONSUMER_SECRET = u''

1. Set the name of your app:

    APP_NAME = u''

1. Set the username of your bot twitter account:

    BOT_SCREEN_NAME = u''

1. Set the name of the file that holds the OAuth token and secret (default computes to ~/.twitter_bot_oauth):

    TOKEN_FILENNAME = u''  

1. Set the keywords you want to follow:

    KEYWORDS = u'#hackersinthepub,#hitp'

1. Login to the bots twitter account in a browser.

1. Run the script. A browser will open and ask you if you want to authenticate the application, say yes.

    python hitp_twitter_bot.py

1. Type the PIN number shown into the terminal.

1. ???

1. PROFIT!


About
-----
Built using: https://github.com/sixohsix/twitter
