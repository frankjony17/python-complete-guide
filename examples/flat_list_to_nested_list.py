"""
    Write a Flat function to make a flat list of a nested list.

    Expected output:
        [1, 2, 3, 10, 4, 5, 6, 7, 8, 9]
"""

_list = [[1, [[2], 3]], [10], [[[4], 5], 6], [7, [8], [9]]]


def flat_list(item):
    _list = []

    for v in item:
        if type(v) == list:
            for j in flat_list(v):
                _list.append(j)
        else:
            _list.append(v)

    return _list


print(flat_list(_list))


""" Solution 2 """


def flatten(_list):
    return [
        element for item in _list for element in flatten(item)] if type(_list) is list else [_list]


print("Transformed List ", flatten(_list))

