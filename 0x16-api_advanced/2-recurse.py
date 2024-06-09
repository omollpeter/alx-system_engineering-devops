#!/usr/bin/python3
"""
This script sends requests recursively to an API and retrieve all the
hot articles from a particular subreddit
"""


import requests


def recurse(subreddit, hot_list=[]):
    """
    Make recursive calls to an API
    """
    after = None
    return recursive(subreddit, hot_list, after)


def recursive(subreddit, hot_list=[], after=None):
    """
    Retrieves all the hot articles of a particular subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Omollo's App"}
    params = {'limit': 100, 'after': after} if after else {'limit': 100}

    response = requests.get(url=url, headers=headers, params=params)
    data = response.json()

    articles = data["data"]["children"]
    if not articles:
        return hot_list

    for article in articles:
        hot_list.append(article["data"])

    after = data.get("data").get("after")
    if after:
        recursive(subreddit, hot_list, after)

    return hot_list
