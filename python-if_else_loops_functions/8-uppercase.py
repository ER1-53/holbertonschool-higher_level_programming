#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord('a') <= ord(str[i]) <= ord('z'):
            maj = ord(str[i]) - 32
            upp = chr(maj)
        else:
            upp = str[i]
        print("{}".format(upp), end='')
    print()
