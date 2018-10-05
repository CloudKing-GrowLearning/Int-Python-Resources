import pandas as pd
import matplotlib.pyplot as plt
import os

file_dir = os.getcwd()

file_name = file_dir + '/word_counts.csv'
word_counts = pd.read_csv(file_name)
file_name = file_dir + '/comment_author_counts.csv'
comment_author_counts = pd.read_csv(file_name)
file_name = file_dir + '/duration_data.csv'
duration_data = pd.read_csv(file_name)

top_ten = word_counts['count'][0:10]
top_ten.index = word_counts['word'][0:10]
top_ten.plot(kind='pie')
plt.title('Pie chart to show top 10 common words')
plt.ylabel('')
file_name = file_dir + '/word_counts.pdf'
plt.savefig(file_name)

comment_author_counts = comment_author_counts[comment_author_counts['count']>7]
comment_author_counts.plot.bar('author','count', legend=False, colormap='Dark2')
plt.title('Bar chart to show comment counts by author')
plt.xlabel('Author name')
plt.ylabel('Comment count')
plt.tight_layout()
file_name = file_dir + '/comment_author.pdf'
plt.savefig(file_name)

duration_data.plot.bar('id', 'duration', legend=False, colormap='Dark2')
plt.title('Bar chart to show comment duration by post')
plt.xlabel('Comment id')
plt.ylabel('Duration (hours)')
plt.tight_layout()
file_name = file_dir + '/comment_duration.pdf'
plt.savefig(file_name)