#!/usr/bin/python3
def roman_to_int(roman_string):
    if (type(roman_string) is str or roman_string is not None):
        D = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        X = 0
        if (len(roman_string) >= 2):
            if (roman_string[-2] < roman_string[-1]):
                for n in roman_string:
                    X += sum(map(lambda R: D[R] if R == n else 0, D))
                X = X - D[n] - D[n]
                return (-X)
            else:
                for n in roman_string:
                    X += sum(map(lambda R: D[R] if R == n else 0, D))
                return (X)
        else:
            for n in roman_string:
                X += sum(map(lambda R: D[R] if R == n else 0, D))
            return (X)
    else:
        return (0)
