import tweepy
import pandas as pd

consumer_key = "2naYjsto83ze29CDVcUpGEgCY"  #   (API Key)
consumer_secret = "udLUubAuNpLdcjmfaPey0q2itOykk6GnEWd0qM6Ib4C36X7KO0" #   (API Secret)
access_token = "240431561-gQajsG8aUjT0IQzHjCrN8h5ohcMlgN6nd1vsWbN8"
access_token_secret = "vsE5gaW6jGnNTWZS6I2oKFE1cScdaWb0Gs1D1YuR96KtW"

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

