import praw
import os
import csv


from csv import writer
from os import path
import pathlib
from textblob import TextBlob

pathToSave = "data/"

      
def clear():
    os.system( 'cls' )  

reddit = praw.Reddit(client_id='IvGvwGotLBLBaA',
                    client_secret='kWWiOZ2LvKDy5gUyElLIOWrClAc',
                    username='HopefulHawk6',  
                    password='Wallstreetbets',
                    user_agent='wsbcomp')
sub = reddit.subreddit('wallstreetbets')

#limit is for how many hot posts you would like.
#in this case it would be the current hot post.
wallstreet = sub.hot(limit=1000)
pathsCreated=[]

for post in wallstreet:
    if "Daily Discussion Thread for" in post.title:
        title=post.title
        postid=post.id
        fullpath=pathToSave+str(title)+"_"+str(postid)+".csv"
        pathsCreated.append(fullpath)
        file= pathlib.Path(fullpath)
        if file.exists():
            print(fullpath+"exists")
        else:
            with open(fullpath, 'w', newline='') as file:
                print(fullpath+"created")
        post.comments.replace_more(limit=0)
        all_comments = post.comments.list()
        with open(fullpath,'a+',newline='',encoding='utf-8')as write_obj:
            csvwriter=writer(write_obj)
            for comment in all_comments:
                print("writing to csv file: id:{} comment:{}".format(comment.id,comment.body))
                row=[str(comment.body),str(comment.score),comment.id]
                csvwriter.writerow(row)
            clear()
for paths in pathsCreated:
    print(paths)
print("done")

# file= pathlib.Path(pathToSave+"test.csv")
# if file.exists():
#     print("exists")
# else:
#     with open(pathToSave+'test.csv', 'w', newline='') as file:
#         print("created")
#         print(file)

# subreddit_name = 'nostalgia'
# num_submissions = 2
# r = praw.Reddit(user_agent="getting top posts from a subredit and its submissions", site_name='lamiastella')
# subreddit = r.get_subreddit(subreddit_name)
# top_submissions = subreddit.get_top_from_year(limit = num_submissions, comment_sort='top')
# for submission in top_submissions:
#         submission.replace_more_comments(limit=None, threshold=0)
#         all_comments = praw.helpers.flatten_tree(submission.comments)
#         if len(all_comments) > 100:
#                 print(len(all_comments)        all_comments = praw.helpers.flatten_tree(submission.comments))
#                 #top_comments = all_comments.sort(key = lambda comment : comment.score, reverse = True)
#                 for comment in all_comments[:10]:
#                         print(comment.body)
#         else:
#                 continue


# reddit = praw.Reddit(client_id='IvGvwGotLBLBaA',
#                     client_secret='kWWiOZ2LvKDy5gUyElLIOWrClAc',
#                     username='HopefulHawk6',  
#                     password='Wallstreetbets',
#                     user_agent='wsbcomp')
# sub = reddit.subreddit('wallstreetbets')
# wallstreet = sub.hot(limit=1)
# for post in wallstreet:
#     print(post.title)
#     comments = post.comments
#     for comment in comments:
#         sentence = TextBlob(comment.body)
#         score=sentence.sentiment.polarity
#         if score > 0:
#             if score > 0.4:
#                 print("Positive: "+comment.body)
#             else: 
#                 print("Somewhat Positive: "+comment.body)
#         else:
#             print("Negative: "+comment.body)


