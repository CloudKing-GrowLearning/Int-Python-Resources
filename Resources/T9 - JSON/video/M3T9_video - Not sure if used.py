#!/usr/bin/python
import tweepy
consumer_key = ""  #   (API Key
consumer_secret = "" #   (API Secret)
access_token = ""
access_token_secret = ""

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