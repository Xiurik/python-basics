# pip install tweepy
# config.py : where I keep my keys as constants
import time

import config
import tweepy


def about_me(client: tweepy.Client) -> None:
    """Print information about the client's user."""
    # The `public_metrics` addition will give me my followers count, among other things
    me = client.get_me(user_fields=["public_metrics"])
    print(f"My name: {me.data.name}")
    print(f"My handle: @{me.data.username}")
    print(f"My followers count: {me.data.public_metrics['followers_count']}")
 
 
def get_ztm_tweets(client: tweepy.Client) -> list[tweepy.Tweet]:
    """Return a list of latest ZTM tweets"""
    ztm = client.get_user(username="zerotomasteryio")
    response = client.get_users_tweets(ztm.data.id)
    return response.data
 

auth = tweepy.OAuthHandler(config.API_KEY, config.API_KEY_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

user = api.me()
print (user.name) #prints your name.
print (user.screen_name)
print (user.followers_count)

search = "zerotomastery"
numberOfTweets = 2

def limit_handle(cursor):
  while True:
    try:
      yield cursor.next()
    except tweepy.RateLimitError:
      time.sleep(1000)

#Be nice to your followers. Follow everyone!
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
  if follower.name == 'Usernamehere':
    print(follower.name)
    follower.follow()


# Be a narcisist and love your own tweets. or retweet anything with a keyword!
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
 
 
if __name__ == "__main__":
    client = tweepy.Client(
        bearer_token=config.BEARER_TOKEN,
        consumer_key=config.API_KEY,
        consumer_secret=config.API_KEY_SECRET,
        access_token=config.ACCESS_TOKEN,
        access_token_secret=config.ACCESS_TOKEN_SECRET,
    )
    
    print("=== About Me ===")
    about_me(client)
    print()
    print("=== ZTM Tweets ===")
    
    
    for tweet in get_ztm_tweets(client):
        print(tweet, end="\n\n")
