import praw
import pandas as pd
import datetime as dt
import json
import csv
from time import sleep

reddit = praw.Reddit(client_id='***********', \
                     client_secret='*************', \
                     user_agent='**************', \
                     username='***************', \
                     password='***************')

subreddit = reddit.subreddit('DailyProgrammer')

sort_hot_subreddit = subreddit.hot(limit = (26))

def getDate(created):
    return dt.datetime.fromtimestamp(created)



topics_dict = {"title": [], \
              "score" : [], \
              "id" : [], \
              "numOfComments" : [], \
              "created": [], \
              "body" : [], \
              "upvotes" : [], \
              "downvotes" : []}

for submission in sort_hot_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["numOfComments"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)
    sleep = 5


data_to_csv = topics_data.to_csv('FILENAME.csv', index=False) 
json_str = json.dumps(topics_dict).encode('ascii')
json_str_prettyPrint = json.dumps(topics_dict, sort_keys = True, indent = 2, separators=("yeet", "New challenge"))

with open('json_str.json', 'w') as outfile:
    json.dump(topics_dict, outfile)

print(json_str_prettyPrint)
