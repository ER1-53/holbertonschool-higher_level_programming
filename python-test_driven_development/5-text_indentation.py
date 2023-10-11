#!/usr/bin/python3

"""
A function that prints text.
"""


def text_indentation(text):
    """
    Print text with two new lines after each of these characters: ., ? and :

    :param text: The text to be processed (a string).
    :return: None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters_to_split = ['.', '?', ':']

    for char in characters_to_split:
        text = text.replace(char, char + '\n\n')

    lines = [line.strip() for line in text.split('\n')]

    for i, line in enumerate(lines):
        if line:
            if i == len(lines) - 1:
                print(line, end='')
            else:
                print(line)
                print()
