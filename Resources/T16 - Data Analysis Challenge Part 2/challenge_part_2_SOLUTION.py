import pandas as pd
import os

file_dir = os.getcwd()
stop_gap_file_name = file_dir + '/common_words.csv'

f = open(stop_gap_file_name, 'r')
data = f.read().split('\n')
stop = []
for d in data:
    stop.append(d)

file_name = file_dir + '/topics_data.csv'

data = pd.read_csv(file_name)

words = []
for ind, row in data.T.iteritems():
    details = row['comment_body'].lower().split(' ')
    for d in details:
        if d not in stop:
            words.append(d)


word_series = pd.Series(words)

word_counts = word_series.value_counts()
word_counts = word_counts[0:100]
word_counts_df = pd.DataFrame({'word': word_counts.index, 'count': word_counts})
file_name = file_dir + '/word_counts.csv'
word_counts_df.to_csv(file_name, index=False)

comment_author_counts = data['comment_author'].value_counts()
comment_author_counts_df = pd.DataFrame({'author': comment_author_counts.index, 'count': comment_author_counts})
file_name = file_dir + '/comment_author_counts.csv'
comment_author_counts_df.to_csv(file_name, index=False)

data['created'] = pd.to_datetime(data['created'])
data['comment_created'] = pd.to_datetime(data['comment_created'])

unique_submission_ids = data['id'].unique()

comment_duration_dict = {'id':[], 'duration': []}

for usi in unique_submission_ids:
    submission_data = data[data['id'] == usi]
    created = submission_data['created'].unique()
    if len(created) > 1:
        print("More than one created value")
        continue
    created = created[0]
    min_comment = submission_data['comment_created'].min()
    max_comment = submission_data['comment_created'].max()
    comment_duration = max_comment - min_comment
    comment_duration_dict['id'].append(usi)
    comment_duration_dict['duration'].append(comment_duration.seconds/60.0/60.0)

duration_data_df = pd.DataFrame(comment_duration_dict)
file_name = file_dir + '/duration_data.csv'
duration_data_df.to_csv(file_name, index=False)
