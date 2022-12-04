import tweepy
import json


append_to_database = True
client = tweepy.Client(
    "Your Token Here"
)
search_ls = ["english", "words", "sophisticated"]
tweet_dict = {}

if append_to_database:
    with open("databse.json", "r") as f:
        data = json.load(f)
        if list(data.keys())[-1].isnumeric():
            tweet_id = int(list(data.keys())[-1]) + 1
else:
    tweet_id = 0

for search_word in search_ls:
    response = client.search_recent_tweets(search_word, max_results=30)
    tweets = response.data
    tweet_list = []
    for tweet in tweets:
        tweet_text = tweet.text.replace("\n", " ")
        if tweet_text not in tweet_list:
            tweet_list.append(tweet_text)
    for tweet_text in tweet_list:
        added_tweet = {
            "text": tweet_text,
            "native count": 0,
            "native positive": 0,
            "nonnative count": 0,
            "nonnative positive": 0,
        }
        tweet_dict[tweet_id] = added_tweet
        tweet_id += 1

if append_to_database:
    data.update(tweet_dict)
    tweet_dict = data

with open("databse.json", "w") as f:
    json.dump(tweet_dict, f, indent=4, separators=(", ", ": "))
