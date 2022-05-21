#!/usr/bin/python3
""" Return list containing the titles of all hot articles """
from requests import request


def recurse(subreddit, hot_list=[], after=""):
    """ Query Reddit API to return all got articles """
    url = "https://api.reddit.com/r/{}/hot?after={}".format(subreddit, after)
    headers = {"User-Agent": "Python3"}
    response = request("GET", url, headers=headers).json().get('data')
    try:
        after = response.get('after', None)
        for item in response.get('children'):
            hot_list.append(item.get('data').get('title'))
        if after is not None:
            recurse(subreddit, hot_list, _after)
        return hot_list
    except Exception:
        return None
