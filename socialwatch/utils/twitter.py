from tweepy import Cursor
from tweepy import OAuthHandler
from tweepy import API

ckey = '2lLcB1zHTBFIksGCYhiP1tPur'
csecret = 'h8DlwdLrepqATIqbq2V7oLRkWxEBVS4ad9RlhdrPHe2ofCG0GJ'
atoken = '3014982345-DtL7wx9trlC7A4B8VQGxSulry1greYDoxKammLd'
asecret = 'CChdoQS4G9E6iZ0NsehCW91SaHDmemmwrGdJORRtcWVJx'


def get_twitter_auth():
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    return auth


def get_twitter_client():
    """

    :rtype: object
    """
    auth = get_twitter_auth()
    client = API(auth)
    return client

