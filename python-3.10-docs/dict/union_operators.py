# https://peps.python.org/pep-0584/

"""
    PEP 584 – Add Union Operators To dict
    This PEP proposes adding merge (|) and update (|=) operators to the built-in dict class.
"""

""" 1
    Dictionary unpacking {**d1, **d2}
    
    A double asterisk ** denotes dictionary unpacking.
    
    {**d1, **d2} ignores the types of mappings and always returns a dict.
"""

dict_1 = {'d1a': 1, 'd1b': 2}
dict_2 = {'d2a': 2, 'd2b': 3}
dict_3 = {'d3c': 2, 'd3d': 4}

dict_4 = {**dict_1, **dict_2, **dict_3}

print(dict_4)  # {'d1a': 1, 'd1b': 2, 'd2a': 2, 'd2b': 3, 'd3c': 2, 'd3d': 4}


""" 2
    collections.ChainMap 
    
    A ChainMap groups multiple dictionaries or other mappings together
    to create a single, updateable view.
    
    Return type is collections.ChainMap.
    We can convert to dict using the dict() constructor.
"""
from collections import ChainMap

dict_1 = {'a': 1,'b': 2}
dict_2 = {'c': 3,'b': 9999}

dict_3 = ChainMap(dict_1, dict_2)

print(dict_3)  # ChainMap({'a': 1, 'b': 2}, {'c': 3, 'b': 9999})
print(dict(dict_3))  # {'c': 3, 'b': 2, 'a': 1}

"""" if we modify the ChainMap object, dict_1 will also be modified.dict_3 = ChainMap(dict_1, dict_2) """
dict_3['a'] = 555555
print(dict_1)  # {'a': 555555, 'b': 2}


""" 3
    dict(d1, **d2)
    
    This “neat trick” is not well-known, and only works when d2 is entirely string-keyed:
    
    If int is given as a key in dict_2, it will raise TypeError.
"""
dict_1 = {'a': 1, 'b': 2}
dict_2 = {'c': 3, 'b': 9999}

dict_3 = dict(dict_1, **dict_2)
print(dict_3)  # {'a': 1, 'b': 9999, 'c': 3}


""" 4
    # https://peps.python.org/pep-0584/#specification
    New Ways Introduced in Python 3.9
    Dict union
    Specification
    
    Dict union will return a new dict consisting of the left operand merged with the right operand,
    each of which must be a dict (or an instance of a dict subclass). 
    If a key appears in both operands, the last-seen value (i.e. that from the right-hand operand) wins:
"""
dict_1 = {'spam': 1, 'eggs': 2, 'cheese': 3}
dict_2 = {'cheese': 'cheddar', 'aardvark': 'Ethel'}

dict_3 = dict_1 | dict_2  # {'spam': 1, 'eggs': 2, 'cheese': 'cheddar', 'aardvark': 'Ethel'}
dict_4 = dict_2 | dict_1  # {'cheese': 3, 'aardvark': 'Ethel', 'spam': 1, 'eggs': 2}

""" The augmented assignment version operates in-place """
dict_1 |= dict_2
print(dict_1)  # {'spam': 1, 'eggs': 2, 'cheese': 'cheddar', 'aardvark': 'Ethel'}
