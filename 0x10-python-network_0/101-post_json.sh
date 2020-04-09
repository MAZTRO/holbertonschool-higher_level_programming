#!/bin/bash
# Script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -s -X POST -H "Accept: application/json" -H "Content-Type: application/json" -d @"$2" "$1"
