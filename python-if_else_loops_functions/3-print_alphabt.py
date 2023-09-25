#!/usr/bin/python3
for ascii in range(97, 123):
    if chr(ascii) != 'q' or chr(ascii) != 'e':
        print(chr(ascii), end='')
