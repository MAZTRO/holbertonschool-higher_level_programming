#!/usr/bin/python3
"""
    Python script that takes in a URL,
    sends a request to the URL and displays the value of the
    X-Request-Id variable found in the header of the response.
"""
import urllib.request
import sys

if __name__ == "__main__":
    av = sys.argv
    with urllib.request.urlopen(av[1]) as response:
        print(response.getheader('X-Request-Id'))
