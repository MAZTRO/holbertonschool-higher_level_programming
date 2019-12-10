#!/usr/bin/python3
for numb_1 in range(0, 10):
    for numb_2 in range(numb_1 + 1, 10):
        if numb_1 < 8 and numb_2 < 10:
            print("{:d}{:d}".format(numb_1, numb_2), end=', ')
        else:
            print("{:d}{:d}".format(numb_1, numb_2))
