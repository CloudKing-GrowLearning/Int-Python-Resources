import praw

reddit = praw.Reddit(client_id='yourid',
                     client_secret='yourclientsecret',
                     username='yourusername',
                     password='yourpassword',
                     user_agent='my user agent')

subreddit = reddit.subreddit('movies')
