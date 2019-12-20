#!/usr/bin/python3
def roman_to_int(roman_string):
    if (type(roman_string) is not str or roman_string is None):
        return (0)
    else:
        D = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        X = 0
        Y = 0
        if (len(roman_string) >= 2):
            if (roman_string[-2] < roman_string[-1]):
                for n in roman_string:
                    X += sum(map(lambda R: D[R] if R == n else 0, D))
                if (len(roman_string) > 2):
                    for a in range(len(roman_string) - 1, 1, -1):
                        print(D[roman_string[a]])
                        if (roman_string[a - 1] < roman_string[a]):
                            Y += D[roman_string[a - 1]]
                    X = X - (Y * 2)
                else:
                    X -= D[roman_string[-2]] * 2
                if (X < 0):
                    return (-X)
                else:
                    return (X)
            else:
                for n in roman_string:
                    X += sum(map(lambda R: D[R] if R == n else 0, D))
                return (X)
        else:
            for n in roman_string:
                X += sum(map(lambda R: D[R] if R == n else 0, D))
            return (X)
