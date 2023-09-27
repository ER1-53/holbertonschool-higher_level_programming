#!/usr/bin/python3
import sys
argv = sys.argv
argc = len(argv)
if len(argv) != 1:
    print("{} arguments:".format(argc))
    for i in range(1,argc):
        print("{}: {}".format(i, argv[i]), end='')
        print()
else:
    print("{} argument.".format(argc))
        