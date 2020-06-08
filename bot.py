import re
import os
import praw


MESSAGE = "Hello! /u/oneplusuna is an attempt by OnePlus to show that they are active in supporting their devices and community. They have provided no support to users as of recently. In the past they at least sent an actual direct message, but did not assist you with the problem any further. Beep boop, I'm a bot designed to call out the atrocious support that OnePlus offers. Created by /u/thecarrotstick."

print(MESSAGE)

if not os.path.isfile('replied.txt'):
    replied = []
else:
    with open("replied.txt", "r") as f:
       replied = f.read()
       replied = replied.split("\n")
       replied = list(filter(None, replied))

with open("replied.txt", "r") as f:
    replied = f.read()
    replied = replied.split("\n")

replied = list(filter(None, replied))

reddit = praw.Reddit('bot1')
subreddit=reddit.subreddit('oneplus')


for comment in subreddit.comments(limit=500000):
    if comment.author == 'oneplusuna':
        if comment.id not in replied:
            comment.downvote()
            comment.reply(MESSAGE)
            replied.append(comment.id)

with open("replied.txt", "w") as f:
    for post_id in replied:
        f.write(post_id + "\n")
        