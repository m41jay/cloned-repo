#!/usr/bin/python3
"""
query the Reddit API and prints the titles of the first 10 hot posts
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    prints titles of hot 10 posts
    """
    if subreddit is None or type(subreddit) is not str:
        print(None)
    r = requests.get("http://www.reddit.com/r/{}/hot.json".
                     format(subreddit),
                     headers={
                         "User-Agent": "Holberton API access"},
                     params={"after": after}).json()
    after = r.get("data", {}).get("after", None)
    posts = r.get("data", {}).get("children", None)
    if posts is None or (len(posts) > 0 and posts[0].get("kind") != "t3"):
        if len(hot_list) == 0:
            return None
        return hot_list
    else:
        for post in posts:
            hot_list.append(post.get("data", {}).get("title", None))
    if after is None:
        if len(hot_list) == 0:
            return None
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
