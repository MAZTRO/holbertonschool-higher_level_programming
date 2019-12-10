#!/usr/bin/python3
for count in range(97, 123):
    if count == 113 or count == 101:
        pass
    else:
        print("{:c}".format(count), end='')
