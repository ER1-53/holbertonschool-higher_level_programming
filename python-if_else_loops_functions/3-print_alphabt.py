#!/usr/bin/python3
for ascii in range(97,123):
    char = chr(ascii)
    if char == 'q' or char == 'e':
        continue
    else:
        print(char, end='')