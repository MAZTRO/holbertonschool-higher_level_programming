#!/usr/bin/python3
def roman_to_int(roman_string):
    if (type(roman_string) is not str or roman_string is None):
        return (0)
    else:
        D = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        X, Y = 0, 0
        if (len(roman_string) >= 2):
            if (roman_string[-2] < roman_string[-1]):
                for n in roman_string:
                    X += sum(map(lambda R: D[R] if R == n else 0, D))
                R = roman_string
                L = range(len(roman_string) - 1, 0, -1)
                Y = sum(map(lambda z: D[R[z - 1]] if D[R[z]] > D[R[z - 1]]
                        else 0, L))
                X = X - (Y * 2)
                return (X)
            else:
                for n in roman_string:
                    X += sum(map(lambda R: D[R] if R == n else 0, D))
                return (X)
        else:
            for n in roman_string:
                X += sum(map(lambda R: D[R] if R == n else 0, D))
            return (X)
