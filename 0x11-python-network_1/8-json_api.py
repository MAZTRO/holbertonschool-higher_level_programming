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

    if (len(av) > 1):
        value = {'q': av[1]}
    else:
        value = {'q': ""}

    req = requests.post('http://0.0.0.0:5000/search_user', data=value)
    try:
        json = req.json()
        if (len(req.json()) == 0):
            print("No result")
        else:
            print("[{}] {}".format(json['id'], json['name']))
    except ValueError:
        print("Not a valid JSON")
