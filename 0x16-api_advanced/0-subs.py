#!/usr/bin/python3
"""Module fires a request to Reddit API
and returns the number of subscribers
"""
from requests import get


def number_of_subscribers(subreddit):
    """Function returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = get(url, allow_redirects=False)
    if response.status_code == 200:
        return int(response.json().get('data', {}).get('subscribers', []))
    return 0
