#!/usr/bin/python3
"""Contains the recurse api function"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    if subreddit is None:
        return None
    url = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'user-agent': 'Kenneth'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        after = response.json()["data"]["after"]
        posts = response.json()["data"]["children"]
        if posts is None:
            if len(hot_list) == 0:
                return hot_list
        else:
            for x in posts:
                hot_list.append(x.get('data', {}).get('title', None))
        if after is None:
            if len(hot_list) == 0:
                return None
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
