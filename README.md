This repository contains the source code of the [SubsYouFellForBot](https://www.reddit.com/user/SubsYouFellForBot). [SubsYouFellForBot](https://www.reddit.com/user/SubsYouFellForBot) is a Reddit bot which upon finding a potential subreddit name in a comment, tries to find if the subreddit exists and comments `r/subsyoufellfor` if it doesn't.

For more information see:
- [The /r/SubsYouFellFor subreddit](https://www.reddit.com/r/SubsYouFellFor/)
- [Praw](https://praw.readthedocs.io/en/latest/)

## Making it work
To make it to work you need to supply a praw.ini file in the directory in which the script is located. An example file might look like this:
```ini
[subsyoufellforbot]
client_id=<your client id here>
client_secret=<your client server here>
password=youfellforthatsubdidyou
username=SubsYouFellForBot
user_agent="SubsYouFellForBot v1.0 (by /u/lilsegmentationfault)"
```
Client id and server can be obtained by setting a Reddit application [here](https://www.reddit.com/prefs/apps).
