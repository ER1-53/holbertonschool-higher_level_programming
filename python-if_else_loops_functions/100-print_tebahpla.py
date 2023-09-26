#!/usr/bin/python3
for ascii in reversed(range(97, 123)):
    if ascii % 2 == 0:
        upp = ascii
    else:
        upp = ascii - 32
    print("{}".format(chr(upp)), end='')
