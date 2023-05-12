#!/usr/bin/python3
""" a function that queries the Reddit API and returns the number of subscribers """

import requests


def number_of_subscribers(subreddit):
    """ a function that queries the Reddit API and returns the
    number of subscribers for a given subreddit """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-agent": "eyatuphilipesamu"}

    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data.get("data").get("subscribers")
        return subscribers
    else:
        return 0
