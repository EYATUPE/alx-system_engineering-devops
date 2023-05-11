#!/usr/bin/python3
""" a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0 """

import requests


def number_of_subscribers(subreddit):
    """ a function that queries the Reddit API and returns the
    number of subscribers for a given subreddit """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header_profile = {"User-agent": "eyatuphilipesamu"}

    response = requests.get(url, header_profile=header_profile, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return (data['data']['subscribers'])
    else:
        return 0
