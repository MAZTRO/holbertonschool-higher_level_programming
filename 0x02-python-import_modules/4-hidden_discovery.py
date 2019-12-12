#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for fold in dir(hidden_4):
        if (hidden_4[0] != '_' and hidden_4[1] != '_'):
            print("{:s}".format(fold))

