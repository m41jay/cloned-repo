#!/usr/bin/python3
"""
A recursive function that counts given words(case-insensitve)
"""

import requests
import sys
after = None
counter = []


def count_words(subreddit, word_list):
    """
    count words
    """
    global after
    global counter
    headers = {"User-Agent": "bluntdoc369"}
    api_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {"after": after}
    response = requests.get(api_url, headers=headers, allow_redirects=False,
                            params=parameters)
