#!/usr/bin/python3
""" File to fetch a url """
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        res = response.read()
    print("Body response:")
    print("\t- type: ", type(res))
    print("\t- content: ", res)
    print("\t- utf8 content: ", res.decode())
