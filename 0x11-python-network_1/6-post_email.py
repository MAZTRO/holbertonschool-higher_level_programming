#!/usr/bin/python3
"""
    Python script that takes in a URL,
        sends a request to the URL and displays
        the body of the response (decoded in utf-8).
"""
import requests
import sys

if __name__ == "__main__":
    av = sys.argv

    value = {'email': av[2]}
    req = requests.post(av[1], data=value)
    print(req.text)
