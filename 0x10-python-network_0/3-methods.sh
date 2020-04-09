#!/bin/bash
# Script that takes in a URL and displays all HTTP methods the server will accept
curl -sI "$1" | awk '/Allow:/ {print $2 " " $3 " " $4}' # curl -sI "$1" | awk '/Allow:/ {for(x=2;x<=NF;++x){printf "%s", $x}; printf "\n"}' // curl -sI "$1" | awk '/Allow:/ {$1=""; print}'
