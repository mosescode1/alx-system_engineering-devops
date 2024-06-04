#!/usr/bin/python3
"""Module fires a request to Reddit API
and returns the number of subscribers
"""
import requests
import sys
argv = sys.argv[1]


def number_of_subscribers(subreddit):
    """Function returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    return 0
