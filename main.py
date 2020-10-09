import json
import tweepy
from collectors import ConsoleCollector, LanguageFilterCollector


def get_api(credentials):
    auth = tweepy.OAuthHandler(credentials['api_key'], credentials['api_secret_key'])
    auth.set_access_token(credentials['access_token'], credentials['access_token_secret'])

    return tweepy.API(auth)


def main(credentials):
    api = get_api(credentials)

    consoleStream = LanguageFilterCollector('en')
    stream = tweepy.Stream(auth=api.auth, listener=consoleStream)
    stream.filter(track=['trump'])


if __name__ == "__main__":
    with open('./credentials.json', 'r') as f:
        credentials = json.load(f)
    main(credentials)
