#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            concat = ord(char) - 32
        else:
            concat = ord(char)
        print("{:c}".format(concat), end='')
    print("")
