#!/usr/bin/python3
"""
Add two value, a and b
>>> a is an integer
>>> b is an integer
function open
"""

def add_integer(a, b=98):
    """
    rasta far Hai..
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)