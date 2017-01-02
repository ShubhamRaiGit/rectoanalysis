from tweepy import Cursor
from socialwatch.utils import twitter

if __name__ == '__main__':
    client = twitter.get_twitter_client()
    for status in Cursor(client.home_timeline).items(10):
    # Process a single status
        print(status.text)