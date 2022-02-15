#!/usr/bin/python3
"""
returns the number of subscribers (not active users, total subscribers)
for a given sureddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers for a given subreddit
    """
    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get("http://www.reddit.com/r/{}/about.json".format(subreddit),
                     headers={"User-agent": "Holberton API acesss
                              v.1.0.0 (by / u/bluntdoc369)"}).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs
