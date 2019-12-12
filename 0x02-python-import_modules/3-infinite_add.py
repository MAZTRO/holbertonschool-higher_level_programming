#!/usr/bin/python3
import sys
if __name__ == "__main__":
    total = 0
    for arguments in sys.argv[1:]:
        total += int(arguments)
    print("{:d}".format(total))
