#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, encoding='utf-8') as lines:
        return len(lines.readlines())
