import snscrape.modules.twitter as sntwitter
import pandas as pd
from textblob import *

def get_tweets(n):
    # Creating list to append tweet data to
    attributes_container = []

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(str('#loveisland')).get_items()):
        if i>n:
            break
        if (tweet.sourceLabel == 'Twitter for Android' or tweet.sourceLabel == 'Twitter for iPhone'):
            attributes_container.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])
        
    return attributes_container

def find_op(tweets):
    overwhelm_positive = []
    for tweet in tweets:
        testimonial = TextBlob(tweet[4])
        if testimonial.sentiment.polarity > 0.3:
            overwhelm_positive.append(tweet)
    return overwhelm_positive

def find_on(tweets):
    overwhelm_negative = []
    for tweet in tweets:
        testimonial = TextBlob(tweet[4])
        if testimonial.sentiment.polarity < -0.3:
            overwhelm_negative.append(tweet)
    return overwhelm_negative

def find_proportion(contestant, tweets):
    count=0
    for tweet in tweets:
        if contestant.upper() in tweet[4].upper():
            count+=1
    return round(count/len(tweets), 4)*100

contestants = ["Luca", "Davide", "Adam", "Dami", "Billy", "Andrew", "Deji",
"Gemma", "Paige", "Ekin", "Indiyah", "Danica", "Tasha", "Summer"]

tweets = get_tweets(50000)
print(len(tweets))
pos_tweets = find_op(tweets)
neg_tweets = find_on(tweets)

for contestant in contestants:
    proportion_pos = find_proportion(contestant, pos_tweets)
    proportion_neg = find_proportion(contestant, neg_tweets)
    print(contestant + "," + str(proportion_pos) + "," + str(proportion_neg))