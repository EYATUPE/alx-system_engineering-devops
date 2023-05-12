#!/usr/bin/python3
""" a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit
"""

from requests import get


def top_ten(subreddit):
    """  prints the titles of the first 10 hot posts listed for a given subreddit """
    head = {"User-Agent": "eyatuphilipessamu"}
    Url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = get(Url, headers=head, allow_redirects=False)
    posts = response.json()
    if response.status_code == 200:
        people = posts.get("data").get("people")
        for post in people:
            print(post["data"]["title"])
    else:
        print("None")
