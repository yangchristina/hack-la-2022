import pandas as pd
from functools import reduce
enr = pd.read_csv('../data/additional/enrollments.csv', sep=',')
enr2 = enr.rename(columns={'user_id': 'Student'})

# disc_count
disc = pd.read_csv('../data/additional/discussions.csv', sep=',')
disc = disc[disc['actor_id'].str.startswith("LEARNER_")]
disc_count = disc[['actor_id']]
disc_count = disc_count.value_counts().rename_axis('actor_id').reset_index(name='disc_count')
disc_count = disc_count.rename(columns={'actor_id': 'Student'})

# mean post_message_length
disc_post_length = disc[['actor_id', 'post_message_length']]
disc_post_length = disc_post_length.groupby('actor_id').mean().reset_index()
disc_post_length = disc_post_length.rename(columns={'actor_id': 'Student', 'post_message_length': 'avg_post_message_length'})

# total likes from posts
total_likes = disc[['actor_id', 'count_of_likes']]
total_likes = total_likes.groupby('actor_id').sum().reset_index()
total_likes = total_likes.rename(columns={'actor_id': 'Student', 'count_of_likes': 'total_likes'})

# avg num of posts per discussion topic

nav = pd.read_csv('../data/navigation_events.csv', sep=',')
total = nav[['actor_id']]
total2 = total.value_counts().rename_axis('actor_id').reset_index(name='nav_count')
total2 = total2[total2['actor_id'].str.startswith("LEARNER_")]
total2 = total2.rename(columns={'actor_id': 'Student'})

gb = pd.read_csv('../data/additional/gradebook.csv', sep=',', skiprows=range(1, 3))

data_frames = [enr2, gb, total2, disc_count, disc_post_length, total_likes]
df = reduce(lambda  left,right: pd.merge(left,right,on=['Student'],
                                            how='outer'), data_frames)

df = df.sort_values(by='Student', key=lambda col: col.str[8:].astype(int))
df = df.loc[df['type'] == 'StudentEnrollment']
df = df.drop(['type', 'last_attended_at'], axis=1)

# print(df)