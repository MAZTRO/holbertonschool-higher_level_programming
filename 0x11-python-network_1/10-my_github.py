#!/usr/bin/python3
"""
    Python script that takes in a URL,
        sends a request to the URL and displays
        the body of the response (decoded in utf-8).
"""
import requests
import sys

av = sys.argv

auth = {'Authorization': 'token ' + av[2]}
url = "https://api.github.com/users/"
req = requests.get('{}{}'.format(url, av[1]), headers=auth)
json = req.json()
if ('id' not in json):
    print('None')
else:
    print(json['id'])
