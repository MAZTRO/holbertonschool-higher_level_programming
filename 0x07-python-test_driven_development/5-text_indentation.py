#!/usr/bin/python3
"""function that print text remplacing some characters.

    Returns: Nothing, only print
"""


def text_indentation(text):
    """Function that print a text:
        Args:
            text (str): Text to print.
            exceptions = '.' '?' ':'
        Returns:
            Nothing, only print
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
