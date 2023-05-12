#!/usr/bin/python3
"""  a recursive function that queries the Reddit API """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ returns a list containing the titles of all hot articles for a given subreddit """

    headers = {'User-agent': 'eyatu_philip'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=70&after={}".format(
            subreddit, after)

    posts = requests.get(url, headers=headers, allow_redirects=False)

    if posts.status_code == 200:
        posts = posts.json()['data']
        after = posts['after']
        posts = posts['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        if after is not None:
            recurse(subreddit, hot_list, after)
        return (hot_list)
    else:
        return (None)
