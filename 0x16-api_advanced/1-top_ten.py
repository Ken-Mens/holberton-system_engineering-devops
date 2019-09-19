#!/usr/bin/python3
"""
queries to reddit api
"""
import requests


def top_ten(subreddit):
    user = {'User-Agent': 'Kenneth'}
    url = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                       .format(subreddit), headers=user).json()
    try:
        for x in url.get('data').get('children'):
            half = x.get('data')
            print(half.get('title'))
    except Exception:
        print(None)
