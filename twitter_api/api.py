import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #get the consumer & access from Twitter account under Keys and Token tab and paste it as a str
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline() #tweets from your timeline
for tweet in public_tweets:
    print(tweet.text)

search_string = 'python'
numbersOfTweets = 2

#the example below is to follow back the followers

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError: 
        time.sleep(300) 

for follower in limit_handler(tweepy.Cursor(api.followers).items()): 
    if follower.name == 'Bill':
        follower.follow()
        break 

for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
    try:
        tweet.favorite()
        print('I like the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break