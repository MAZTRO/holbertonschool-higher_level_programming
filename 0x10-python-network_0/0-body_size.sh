#!/bin/bash
# Size of the content
curl -s "$1" | wc -c
