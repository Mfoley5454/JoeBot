import praw
import re
from requests import Session
from praw.models import MoreComments


subRedditList = ['todayilearned','writingprompts','copypasta','tifu','askReddit']
writeFile = open("testoutput.txt", "w+")

reddit = praw.Reddit(client_id='AykrCJZQwoCAxA',
                     client_secret='f8hSfCbHiREbEgSJa_RKYaOIOCk',
                     username = 'doritodustgamergunk',
                     password = 'JoeBot2019',
                     user_agent = 'dumbBot by /u/doritodustgamergunk'
                     )
wordCount = 0.0
for submission in reddit.subreddit("writingprompts").top(limit=5):
    comments = submission.comments
    for comment in comments:
        if isinstance(comment, MoreComments):
            continue
        if comment.score > 1000:
            comment.body = re.sub("\n", "", comment.body)
            comment.body = comment.body.replace('\"','')
            comment.body = comment.body.replace('”','')
            comment.body = comment.body.replace('“','')
            writeFile.write(comment.body)
            wordCount += len(comment.body.split(" "))
