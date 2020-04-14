#!/usr/bin/python3
"""
    Python script that takes in a URL and an email,
    sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys

av = sys.argv
url = av[1]
value = {'email': av[2]}

data = urllib.parse.urlencode(value)
data = data.encode('ascii')
with urllib.request.urlopen(av[1], data) as response:
    page = response.read().decode('utf-8')
    print(page)
