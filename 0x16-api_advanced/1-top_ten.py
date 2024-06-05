#!/usr/bin/python3
"""
This script prints the top ten hot topics ina particular subredit
"""


import requests


def top_ten(subreddit):
    """
    Prints the top ten hot topics in a particular subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Omollo's App"}

    response = requests.get(url=url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    data = response.json()
    hot_topics = []
    for t in data.get("data").get("children"):
        hot_topics.append(t.get("data").get("title"))
    i = 0
    for t in hot_topics:
        print(t)
        if i == 9:
            break
        i += 1
