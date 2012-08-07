import os
from twitter.api import Twitter, TwitterError, TwitterHTTPError
from twitter.oauth import OAuth, write_token_file, read_token_file
from twitter.stream import TwitterStream
from twitter.oauth_dance import oauth_dance

APP_NAME = u'Hackers In The Pub bot'

BOT_SCREEN_NAME = u'hackersinthepub'

CONSUMER_KEY = u''

CONSUMER_SECRET = u''

TOKEN_FILENAME = os.environ.get('HOME', '') + os.sep + '.twitter_bot_oauth'

KEYWORDS = u'#hackersinthepub,#hitp'

if __name__ == '__main__':

    try:
        with open(TOKEN_FILENAME) as f: pass
    except IOError as e:
        oauth_dance(APP_NAME, CONSUMER_KEY, CONSUMER_SECRET, TOKEN_FILENAME)

    oauth_token, oauth_token_secret = read_token_file(TOKEN_FILENAME)

    auth = OAuth(
        oauth_token,
        oauth_token_secret,
        CONSUMER_KEY,
        CONSUMER_SECRET
    )

    poster = Twitter(
        auth=auth,
        api_version='1',
        domain='api.twitter.com'
    )

    twitter = TwitterStream(
        auth=auth
    )

    updates = twitter.statuses.filter(track=KEYWORDS)

    for update in updates:
        print(update['id_str'], update['text'])
	
	# Make sure we don't retweet our own retweets
        if update['user']['screen_name'].lower() != BOT_SCREEN_NAME.lower():
            try:
                poster.statuses.retweet(id=update['id'])
                last_id_retweeted = update['id_str']
            except TwitterHTTPError, e:
                pass
