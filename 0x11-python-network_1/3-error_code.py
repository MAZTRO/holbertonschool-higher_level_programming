#!/usr/bin/python3
"""
    Python script that takes in a URL,
    sends a request to the URL and displays
    the body of the response (decoded in utf-8).
"""
import urllib.request
import urllib.parse
import sys

av = sys.argv
try:
        with urllib.request.urlopen(av[1]) as response:
                page = response.read().decode('utf-8')
                print(page)
except urllib.error.URLError as errno:
                print("Error code: ", errno.code)
