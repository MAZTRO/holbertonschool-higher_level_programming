#!/usr/bin/python3
"""
    Python script that takes in a URL,
    sends a request to the URL and displays
    the body of the response (decoded in utf-8).
"""
import requests

req = requests.get('https://intranet.hbtn.io/status')
print("Body response:")
print("\t- type: ", type(req.text))
print("\t- content: ", req.text)
