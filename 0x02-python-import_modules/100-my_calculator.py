#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1

    numb_1 = int(sys.argv[1])
    opp = sys.argv[2]
    numb_2 = int(sys.argv[3])
    if (len(sys.argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if (sys.argv[2] == '+'):
        print("{:d} {:s} {:d}\
 = {:d}".format(numb_1, opp, numb_2, numb_1 + numb_2))
        exit(0)
    elif (sys.argv[2] == '-'):
        print("{:d} {:s} {:d}\
 = {:d}".format(numb_1, opp, numb_2, numb_1 - numb_2))
        exit(0)
    elif (sys.argv[2] == '*'):
        print("{:d} {:s} {:d}\
 = {:d}".format(numb_1, opp, numb_2, numb_1 * numb_2))
        exit(0)
    elif (sys.argv[2] == '/'):
        print("{:d} {:s} {:d}\
 = {:d}".format(numb_1, opp, numb_2, numb_1 // numb_2))
        exit(0)
    elif (sys.argv[2] != '+' or sys.argv[2] != '-'):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    elif (sys.argv[2] != '*' or sys.argv[2] != '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
