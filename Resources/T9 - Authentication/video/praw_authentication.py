import praw
import pandas as pd
import datetime as dt
from my_details import *

reddit = praw.Reddit(client_id='6pt9Q4TZkctkug',
                     client_secret='RfqpmuPrSwZNNZvtn_k9R2Y4Ux4',
                     user_agent='Sage Praw Tutorial',
                     username=user,
                     password=pwd)

subreddit = reddit.subreddit('politics')
#
top_subreddit = subreddit.top('day',limit=5)

topics_dict = {"title": [], "score": [], "id": [], "url": [], "comms_num": [], "created": [], "body": []}

for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(dt.datetime.fromtimestamp(submission.created))
    topics_dict["body"].append(submission.selftext)

topics_data = pd.DataFrame(topics_dict)
print(topics_data)