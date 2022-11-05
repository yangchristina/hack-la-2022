import pandas as pd

# data = pd.read_csv('../data/navigation_events.csv')
# print(data.head())
# print(data["type"])

def get_actors_with_post_message_length():
    discussion_data = pd.read_csv('../data/additional/discussions.csv')
    dict = {}
    for index, row in discussion_data.iterrows():
        curLength = dict.get(row.actor_id)
        if curLength == None:
            curLength = 0
        dict.update({row.actor_id: curLength + row.post_message_length})
    return dict



def get_student_and_current_score():
    data = pd.read_csv('../data/additional/gradebook.csv')
    data = data.drop([0, 1])
    return dict(zip(data["Student"], data["Current Score"]))

if __name__ == "__main__":
    print(get_actors_with_post_message_length())
    print(get_student_and_current_score())