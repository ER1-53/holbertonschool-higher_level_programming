#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] == '+':
        print("{}".format(add(int(argv[1]), int(argv[3]))))
    elif argv[2] == '-':
        print("{}".format(sub(int(argv[1]), int(argv[3]))))
    elif argv[2] == '*':
        print("{}".format(mul(int(argv[1]), int(argv[3]))))
    elif argv[2] == '/':
        print("{}".format(div(int(argv[1]), int(argv[3]))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")


