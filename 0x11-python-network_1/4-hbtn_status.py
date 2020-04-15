#!/usr/bin/python3
"""
    Python script that takes in a URL,
    sends a request to the URL and displays
    the body of the response (decoded in utf-8).
"""
import requests

if __name__ == "__main__":
    req = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
