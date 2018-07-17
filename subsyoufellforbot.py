import praw
import prawcore

def login():
    print("Logging in...")

    r = praw.Reddit("subsyoufellforbot") # referenced in praw.ini 

    print("...logged in!\n")
    return r

def run(reddit, subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    
    comments = subreddit.stream.comments()
    try:
        for comment in comments:
            text = comment.body
            if text.startswith("r/") and " " not in text: # if it may be a subreddit
                try:
                    reddit.subreddit(text).posts().next() # no posts -- doesn't exit
                except prawcore.exceptions.BadRequest:
                    comment.reply("r/subsyoufellfor")
                    print("Found non existing subreddit {0}, commenting...".format(text))
                except Exception as e:
                    print("Exception:", e)
                    continue
    except praw.exceptions.APIException as e:
        print("Exception:", e)

reddit = login()

print("Starting to search for comments...")
while True:
    try:
        run(reddit, "all")
    except KeyboardInterrupt:
        print("\nCtrl + C pressed, exiting...")
        break
    except ValueError as ve:
        print(ve)
        break
print("...searching for comments done!")
