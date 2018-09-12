import praw
from praw.models import MoreComments
import pandas as pd
import datetime as dt
import os
from config import *

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent,
                     username=username,
                     password=passwd)

subreddit = reddit.subreddit('politics')

top_subreddit = subreddit.hot(limit=20)

topics_dict = {"title": [], "score": [], "id": [], "url": [], "comms_num": [], "created": [], "body": [],
               "comment_body": [], "comment_author": [], "comment_created": []}

for submission in top_subreddit:
    all_comments = submission.comments.list()
    for ac in all_comments:
        if isinstance(ac, MoreComments):
            continue
        else:
            topics_dict["title"].append(submission.title)
            topics_dict["score"].append(submission.score)
            topics_dict["id"].append(submission.id)
            topics_dict["url"].append(submission.url)
            topics_dict["comms_num"].append(submission.num_comments)
            topics_dict["created"].append(dt.datetime.fromtimestamp(submission.created))
            topics_dict["body"].append(submission.selftext)
            topics_dict["comment_body"].append(ac.body)
            topics_dict["comment_author"].append(ac.author)
            topics_dict["comment_created"].append(dt.datetime.fromtimestamp(ac.created))

topics_data = pd.DataFrame(topics_dict)
file_dir = os.getcwd()
file_name = file_dir + '/topics_data.csv'
topics_data.to_csv(file_name, index = False)

