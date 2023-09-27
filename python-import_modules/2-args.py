#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)
    if (argc - 1) == 1:
        argu = "argument"
    else:
        argu = "arguments"
    print("{} {}".format(argc - 1, argu), end="")
    if len(argv) != 1:
        print(":")
        for i in range(1,argc):
            print("{}: {}".format(i, argv[i]), end='')
            print()
    else:
        print(".")
        