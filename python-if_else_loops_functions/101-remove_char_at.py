#!/usr/bin/python3
def remove_char_at(str, n):
    for letter in range(len(str)):
        if n < 0 or n >= len(str):
            return (str)
        else:
            return (str[0:n] + str[n + 1:])
