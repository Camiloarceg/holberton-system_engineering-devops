#!/usr/bin/python3
""" Return top ten titles """
import requests


def top_ten(subreddit):
    """ Query Reddit API to return first 10 hot posts """
    header = {'User-Agent': 'my_user_agent'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    try:
        response = requests.get(
            url, headers=header, allow_redirects=False).json().get("data")
        for children in response.get("children"):
            print(children.get("data").get("title"))
    except Exception:
        print(None)
