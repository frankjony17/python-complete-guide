"""
    Given an integer, return the integer with reversed digits.
    Note:
         The integer could be either positive or negative.

"""


def reverse(value):
    str_number = str(value)

    if str_number[0] == '-':
        return int('-' + str_number[:0:-1])

    return int(str_number[::-1])


print(reverse(-231))
print(reverse(345))
