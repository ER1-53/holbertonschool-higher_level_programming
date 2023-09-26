#!/usr/bin/python3
for ascii in range(97, 123):
    if ascii == 101 or ascii == 113:
        continue
    else:
        print("{}".format(chr(ascii)), end='')
