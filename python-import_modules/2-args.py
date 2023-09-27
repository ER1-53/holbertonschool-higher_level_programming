#!/usr/bin/python3
import sys
argv = sys.argv
argc = len(argv)
print("{} arguments".format(argc), end="")
if len(argv) != 1:
    for i in range(1,argc):
        print(":")
        print("{}: {}".format(i, argv[i]), end='')
        print()
else:
    print(".")
        