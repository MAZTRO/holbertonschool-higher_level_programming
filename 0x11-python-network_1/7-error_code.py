#!/usr/bin/python3
"""
    Python script that takes in a URL,
        sends a request to the URL and displays
        the body of the response (decoded in utf-8).
"""
import requests
import sys

av = sys.argv

req = requests.get(av[1])
if (req.status_code == requests.codes.ok):
    print(req.text)
else:
    print("Error code: ", req.status_code)
