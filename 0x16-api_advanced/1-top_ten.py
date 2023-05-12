#!/usr/bin/python3
""" a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit """

import requests


def top_ten(subreddit):
    """  prints the titles of the first 10 hot posts listed for a given subreddit. """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-agent": "eyatuphilipesamu"}

    posts = requests.get(url, headers=headers, allow_redirects=False)

    if posts.status_code == 200:
        for post in posts.json()['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
