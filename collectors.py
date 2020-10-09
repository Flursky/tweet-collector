import tweepy


class LanguageFilterCollector(tweepy.StreamListener):

    def __init__(self, lang):
        self.lang = lang

    def on_status(self, status):
        if status == self.lang:
            print(status.text)


class ConsoleCollector(tweepy.StreamListener):
    def on_status(self, status):
        tweet = {}
        tweet['id'] = status.id
        tweet['text'] = status.text
        tweet['user'] = status.user.screen_name
        tweet['lang'] = status.lang
        tweet['favorite_count'] = status.favorite_count
        tweet['retweet_count'] = status.retweet_count
        print(tweet)


class DBCollector(tweepy.StreamListener):
    pass
