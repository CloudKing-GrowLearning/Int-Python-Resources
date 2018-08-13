import praw
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

reddit = praw.Reddit(client_id='client id',
                     client_secret='client secret',
                     user_agent='Test',
                     username='user',
                     password='pass')

subreddit = reddit.subreddit('movies')

top_subreddit = subreddit.top(limit=5)

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

x = topics_dict["score"]
y = topics_dict["comms_num"]

plt.scatter(x, y)

plt.xlabel('Score')
plt.ylabel('Num of Comments')

plt.xticks(rotation=90)
plt.show()