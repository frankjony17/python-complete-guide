"""
    Given a string, find the first non-repeating character in it and return its index.
    If it doesn't exist, return -1. # Note: all the input strings are already lowercase.
"""

import collections


def unique_character(s):
    # gives back a dictionary with words occurrence count
    # Counter({'l': 1, 'e': 3, 't': 1, 'c': 1, 'o': 1, 'd': 1})
    count = collections.Counter(s)

    # find the index
    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return idx
    return -1


print(unique_character('alphabet'))
print(unique_character('barbados'))
print(unique_character('crunchy'))
