import praw
from config import username as user, password as passwd

reddit = praw.Reddit(client_id='Y6zUEYJKcpeq4w',
                     client_secret='0kPxGl11Fv8br4iKRmoDUYlGPCg',
                     username=user,
                     password=passwd,
                     user_agent='Sage Praw Tutorial')

subreddit = reddit.subreddit('movies')
hot_subreddit = subreddit.hot(limit=5)

for hs in hot_subreddit:
    print(hs.title)
    print(hs.score)