#!/usr/bin/python3
import calculator_1 as calc
import sys
if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] == '+':
        print("{}".format(calc.add(int(argv[1]), int(argv[3]))))
    elif argv[2] == '-':
        print("{}".format(calc.sub(int(argv[1]), int(argv[3]))))
    elif argv[2] == '*':
        print("{}".format(calc.mul(int(argv[1]), int(argv[3]))))
    elif argv[2] == '/':
        print("{}".format(calc.div(int(argv[1]), int(argv[3]))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")


