#!/usr/bin/python3
"""Recursive function that queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[]):
    """Function returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url)
    if response.status_code == 200:
        hot_titles_list = response.json().get("data").get("children")
        for title_data in hot_titles_list:
            hot_list.append(title_data.get("data").get("title"))
        return recurse(subreddit, hot_list)
    else:
        if len(hot_list) == 0:
            return None
        return hot_list
