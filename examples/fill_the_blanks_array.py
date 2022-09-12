"""
    Given an array containing None values fill in the None values with most recent
    non None value in the array
"""

array_1 = [1, None, 2, 3, None, None, 5, None]


def fill_the_blanks(array):
    for i in range(len(array)):
        if array[i] is None:
            array[i] = array[i - 1]
    return array


print(fill_the_blanks(array_1))
