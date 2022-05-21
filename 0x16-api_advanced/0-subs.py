#!/usr/bin/python3
""" Return the number of subs """
import requests


def number_of_subscribers(subreddit):
    """ Query Reddit API to return number of subs of an subreddit """
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    headers = {"User-Agent": "Python3"}
    response = requests.request("GET", url, headers=headers, allow_redirects=False).json()
    try:
        subscribers = response.get('data').get('subscribers')
        return subscribers
    except Exception:
        return 0
