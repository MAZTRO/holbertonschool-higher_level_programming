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

    if (type(text) is not str):
        raise TypeError("text must be a string")
    else:
        count = 0
        if text is not None:
            text = text.strip()
            for idx in text:
                if idx in '.?:':
                    print(idx, end='')
                    count = 1
                    print("\n")
                if (idx != ' ' and count == 1):
                    print(idx, end='')
                count = 0
