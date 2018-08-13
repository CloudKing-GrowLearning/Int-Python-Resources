#!/usr/bin/python
import tweepy
consumer_key = "CxSuk556OxkH2j0an1Vogsy3G"  #   (API Key
consumer_secret = "QSveHPbTS2bBqirXjQAoE28wm1UpbkZZaRLE1MLnhhN2vJTKd4" #   (API Secret)
access_token = "240431561-NQ8bqrAaOAt56MKzi3GK9D4F52f97yMWhHGNvjEL"
access_token_secret = "1DIqANIF2fZV4fzjD2LiD6nP5gBvsPR6eqzHNaeB8rOjn"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.get_user('robertmastro')

# print user.screen_name
# print user.followers_count
# for friend in user.friends():
#    print friend.screen_name
#
#

for status in tweepy.Cursor(api.user_timeline, id="robertmastro").items():
    # process status here
    # print dir(status)
    pass
    # print("__________________________________________________________\n")
    # print("Created at: ",status.created_at)
    # print("Tweet: ", status.text)
    #
    # print("\n__________________________________________________________\n")

print(status._json)

#print(tweepy.Cursor(api.user_timeline, id="robertmastro").items())