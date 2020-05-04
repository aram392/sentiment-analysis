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

#just testing out streams

for comment in sub.stream.comments():
    try:
        print(30*'_')
        print()
        parent_id = str(comment.parent())
        submission = reddit.comment(parent_id)
        print('Parent:')
        print(submission.body.encode("utf-8"))
        print('Reply')
        print(comment.body.encode("utf-8"))
    except praw.exceptions.PRAWException as e:
        pass



#limit is for how many hot posts you would like.




# for post in wallstreet:
#     if "Daily Discussion Thread for" in post.title:
#         title=post.title
#         postid=post.id
#         fullpath=pathToSave+str(title)+"_"+str(postid)+".csv"
#         pathsCreated.append(fullpath)
#         file= pathlib.Path(fullpath)
#         if file.exists():
#             print(fullpath+"exists")
#         else:
#             with open(fullpath, 'w', newline='') as file:
#                 print(fullpath+"created")
#         post.comments.replace_more(limit=0)
#         all_comments = post.comments.list()
#         with open(fullpath,'a+',newline='',encoding='utf-8')as write_obj:
#             csvwriter=writer(write_obj)
#             for comment in all_comments:
#                 print("writing to csv file: id:{} comment:{}".format(comment.id,comment.body))
#                 row=[str(comment.body),str(comment.score),comment.id]
#                 csvwriter.writerow(row)
#             clear()
# for paths in pathsCreated:
#     print(paths)
# print("done")