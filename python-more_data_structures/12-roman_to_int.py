#!/usr/bin/python3
def roman_to_int(roman_string):
    convert = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev_value = 0 
    total = 0
    if roman_string is None or type(roman_string) != str:
        return 0
    for idx in range(len(roman_string)):
        value = convert.get((roman_string[idx]), 0)
        if value > prev_value:
            total += value - 2 * prev_value
        else:
            total += value
        prev_value = value

    return total