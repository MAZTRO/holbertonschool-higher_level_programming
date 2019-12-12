#!/usr/bin/python3
import sys
count = 0
if (len(sys.argv) > 1):
    print("{:d} arguments:".format(len(sys.argv) - 1))
    for w in sys.argv[1:]:
        count += 1
        print("{:d}: {:s}".format(count, w))
else:
    print("{:d} arguments.".format(len(sys.argv) - 1))
