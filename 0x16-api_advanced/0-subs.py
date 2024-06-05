#!/usr/bin/python3
"""
This script makes a get request to Reddit api and retrieves the total
number of subscribers for a particular subreddit
"""


import requests


def number_of_subscribers(subreddit):
    """
    Retrives the total number of subscribers for a particular reddit
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Omollo's Application"}
    response = requests.get(url=url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json()
    return data.get("data").get("subscribers")
