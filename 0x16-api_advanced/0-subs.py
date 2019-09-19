#!/usr/bin/python3
import requests
""" Queries reddit api and returns number of subscribers """


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user = {'User-Agent': 'Kenneth'}
    resp = requests.get(url, headers=user, allow_redirects=False)
    try:
        resp = resp.json()
        subscribers = resp.get('data').get('subscribers')
        return subscribers
    except Exception:
        return 0
