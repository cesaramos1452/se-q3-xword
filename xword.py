#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = "Cesar Ramos"
import re

# YOUR HELPER FUNCTION GOES HERE


def pattern(s):
    s = s.replace(' ', r'[a-z]')
    return s


def main():
    with open('dictionary.txt') as f:
        words = f.read().split()

    test_word = input(
        ("""Please enter a word to solve.\nUse spaces
        to signify unknown letters: """)).lower()

    s = pattern(test_word)

    for word in words:
        if re.match(s, word) and len(word) == len(test_word):
            print(word)


if __name__ == '__main__':
    main()
