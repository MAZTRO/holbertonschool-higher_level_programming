#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = -(number)
    mod = number % 10
else:
    mod = number % 10
last = mod
if last > 5:
    print("Last digit of {:d} is {:d} and is greater\
 than 5".format(number, mod))
elif last == 0:
    print("Last digit of {:d} is {:d} and is zero".format(number, mod))
elif last < 6 and mod != 0:
    print("Last digit of {:d} is {:d} and is less than\
 6 and not 0".format(number, mod))
