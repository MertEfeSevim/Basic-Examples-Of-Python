import twitter
import tweepy
from textblob import TextBlob

def seeTweets(textAnalysis=False):
    topic = input("Which topic you want to search on Twitter ?")

    public_tweets = api.search(topic)

    for tweet in public_tweets:

        print(tweet.text)

        if textAnalysis:

            analysis = TextBlob(tweet.text)
            print(analysis.sentiment)
            print("")

        else:
            print("")

if __name__ == '__main__':
    twitter_consumer_key = 'FbJfLhIMvWu0OSnzVzPvTZs6E'                              # You should take these for yourself
    twitter_consumer_secret = '5T6RXuWdGeCy2M3hvSWU2u5MaYtq0w8IcrHAtZ7D4j46uhNhf0'
    twitter_access_token = '792811803852038144-LbYZggdOWn45Onhiy7zIOgB9NdPfltU'
    twitter_access_secret = 'EkaMYnloUvtRBw6ymPdlqSiKWhuKyLDlPYb3fRb7IAfKq'


    auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
    auth.set_access_token(twitter_access_token, twitter_access_secret)
    api = tweepy.API(auth)

    twitter_stream = twitter_stream(auth=auth)
    #seeTweets()

"""

import wikipedia
import wolframalpha

while True:
    question = input("Q: ")

    try:
        #wolframalpha
        print("Searching in Wolframalpha.")
        app_id = "" #You should take it for yourself
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        answer = next(res.results).text
        print(answer)
    except:
        #wikipedia
        print("Searching in Wikipedia.")
        print(wikipedia.summary(question))
        
"""