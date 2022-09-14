"""
    Write a Flat function to make a flat list of a nested list.

    Expected output:
        [1, 2, 3, 10, 4, 5, 6, 7, 8, 9]
"""

a = [[1, [[2], 3]], [10], [[[4], 5], 6], [7, [8], [9]]]


def flat_list(item):
    _list = []

    for v in item:
        if type(v) == list:
            for j in flat_list(v):
                _list.append(j)
        else:
            _list.append(v)

    return _list


print(flat_list(a))

flat_list = [item for sublist in a for item in sublist]
print(flat_list)
