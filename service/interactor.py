from twitterDriver import get_all_tweets

def buildTweetQuery(text):
    tweets = get_all_tweets(text)
    return tweets