import tweepy
import pandas as pd

consumer_key = ""  #   (API Key)
consumer_secret = "" #   (API Secret)
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.get_user('robertmastro')

created = []
tweet = []

for status in tweepy.Cursor(api.user_timeline, id="robertmastro").items():
    created.append(pd.to_datetime(status.created_at))
    tweet.append(status.text)

data = {'created': created, 'tweet': tweet}
data_df = pd.DataFrame(data)
print(data_df.head())

