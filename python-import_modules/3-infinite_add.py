#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)
    result = 0
    for i in range(1, argc):
        result += int(argv[i])
    print("{}".format(result))
