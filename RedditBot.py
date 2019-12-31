import praw
import modelMaker
from praw.models import MoreComments
import requests
import json

#               CURRENT THINGS TO WORK ON
#Currently reads the comments of a subreddit (writing prompts)
#Possibly do a sweep of top 10 posts for each subreddit mentioned then,
#^^^^ move into the hot posts of each subreddit and check in every few hours for new posts?
#DONE a system to remove punctuation from strings except for '.'
#TODO create a function system of bigrams and trigrams with a strong enough
#^^^^ data pool to support accurate findings
#TODO find best way to store data in database. (Storing bigrams/trigrams with occurances?)(Mongo?)
#TODO find a rest API to implement to support database (Flask???)
#TODO thing below is pretty slow. Must be some way to speed this part up
#TODO find a home for this list of ideas

response = requests.get("http://192.168.1.149:3000/botDB/RedditPosts")
print(response.status_code)
#Subreddits to be looked at based on their posts
subRedditList = ['todayilearned','copypasta','tifu']
#Subreddits to be looked at based on the comments of their posts
subRedditCommentList = ['writingprompts','askReddit']
#List of found punctuation in subreddit posts/comments that should be removed
punctuationList = ['\"','”','“','~',"-","_",'?','*',',','$','#',"\n"]


reddit = praw.Reddit(client_id='AykrCJZQwoCAxA',
                     client_secret='f8hSfCbHiREbEgSJa_RKYaOIOCk',
                     username = 'doritodustgamergunk',
                     password = 'JoeBot2019',
                     user_agent = 'dumbBot by /u/doritodustgamergunk'
                     )

wordCount = 0
for submission in reddit.subreddit("writingprompts").hot(limit=10):
    comments = submission.comments
    for comment in comments:
        if isinstance(comment, MoreComments):
            continue
        if comment.score > 100:
            for char in punctuationList:
                if char == "\n":
                    comment.body = comment.body.replace(char, ' ')
                else:
                    comment.body = comment.body.replace(char, '')
#                print(modelMaker.createBigrams(comment.body))
#Create a module for language modelling to clean up this area of code
#Leave the modelling to another file.
#Have this files only concern being normallizing data from reddit
