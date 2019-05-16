from twitterDriver import get_all_tweets

def buildTweetQuery(text):
    tweets = get_all_tweets(text)
    return tweets

def extract_hash_tags(text):
  """Extracts and returns a set of hashtags found in a text block"""
  return set(part[1:] for part in text.split() if part.startswith('#'))

def extract_handles(text):
  """Extracts twitter handles (aka usernames) found in a text block"""
  return set(part[1:] for part in text.split() if part.startswith('@'))