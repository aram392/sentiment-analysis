import praw
from textblob import TextBlob

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

reddit = praw.Reddit(client_id='IvGvwGotLBLBaA',
                    client_secret='kWWiOZ2LvKDy5gUyElLIOWrClAc',
                    username='HopefulHawk6',
                    password='Wallstreetbets',
                    user_agent='wsbcomp')
sub = reddit.subreddit('wallstreetbets')
wallstreet = sub.hot(limit=1)
for post in wallstreet:
    print(post.title)
    comments = post.comments
    for comment in comments:
        sentence = TextBlob(comment.body)
        score=sentence.sentiment.polarity
        if score > 0:
            if score > 0.4:
                print("Positive: "+comment.body)
            else: 
                print("Somewhat Positive: "+comment.body)
        else:
            print("Negative: "+comment.body)




