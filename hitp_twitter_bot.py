from twitter.api import Twitter, TwitterError, TwitterHTTPError
from twitter.oauth import OAuth, write_token_file, read_token_file
from twitter.stream import TwitterStream

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''
KEYWORDS = '#hackersinthepub,#hitp'

if __name__ == '__main__':
    auth = OAuth(
        OAUTH_TOKEN,
        OAUTH_TOKEN_SECRET,
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
        try:
            poster.statuses.retweet(id=update['id'])
            last_id_retweeted = update['id_str']
        except TwitterHTTPError, e:
            pass
