#!/usr/bin/python3
"""function that adds 2 integers.
    Returns an integer: the addition of a and b.
    a and b must be integers or floats, otherwise raise a TypeError
    exception with the message a must be an integer or b must be an integer
"""


def text_indentation(text):
    """
        a and b must be first casted to integers if they are float
    """

    if (type(text) is not str or len(text) == 0):
        raise TypeError("text must be a string")
    else:
        if text is not None:
            count = 0
            text = text.strip()
            for char in text:
                if (char is ' ' and count == 1):
                    temp = 0
                    continue
                if char in '.?:':
                    print(char, end='')
                    print('\n')
                    count = 1
                else:
                    print(char, end='')
                    count = 0
