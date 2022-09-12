"""
    Create a dictionary with all values multiplied by 2.
    Using 3 o more dictionaries for create a new one.

    dict_1 = {'d1a': 1, 'd1b': 2}
    dict_2 = {'d2a': 2, 'd2b': 3}
    dict_3 = {'d3c': 2, 'd3d': 4}

    Expected result:
        -> {'d1a': 2, 'd1b': 4, 'd2a': 4, 'd2b': 6, 'd3c': 4, 'd3d': 8}
"""
dict_1 = {'d1a': 1, 'd1b': 2}
dict_2 = {'d2a': 2, 'd2b': 3}
dict_3 = {'d3c': 2, 'd3d': 4}

dictionary_1 = {k: v * 2 for k, v in {**dict_1, **dict_2, **dict_3}.items()}

# Best way to do it
dictionary_2 = {k: v * 2 for k, v in (dict_1 | dict_2 | dict_3).items()}

print(dictionary_1)  # {'d1a': 2, 'd1b': 4, 'd2a': 4, 'd2b': 6, 'd3c': 4, 'd3d': 8}
print(dictionary_2)  # {'d1a': 2, 'd1b': 4, 'd2a': 4, 'd2b': 6, 'd3c': 4, 'd3d': 8}

""" Dictionary Comprehensions and merge dict with Union Operator"""
