#!/usr/bin/python3
"""Module fires a request to Reddit API
and returns the top 10 hot posts titles
"""
import requests


def top_ten(subreddit):
    """Function returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=9".format(subreddit)
    response = requests.get(url, allow_redirects=False)
    if response.status_code == 200:
        hot_titles_list = response.json().get("data").get("children")
        for title_data in hot_titles_list:
            print(title_data.get("data").get("title"))
    else:
        print("None")
