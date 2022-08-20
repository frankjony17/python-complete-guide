
# 1 --------------------------------------------------------------------------------------------------------------------
"""
    New Type Union Operator.
    Accepting arguments of multiple types:
"""


def square(number: int | float) -> int | float:
    return number ** 2


# This new syntax is also accepted as the second argument to isinstance() and issubclass():
isinstance(4.0, int | str | float)  # return True for float type.


# 2 --------------------------------------------------------------------------------------------------------------------
"""
    Dictionary Merge & Update Operators:
    Merge (|) and update (|=) operators have been added to the built-in dict class.
    Those complement the existing dict.update and {**d1, **d2} methods of merging dictionaries.
"""

x = {"key1": "value1 from x", "key2": "value2 from x"}
y = {"key2": "value2 from y", "key3": "value3 from y"}

z = x | y  # return -> {'key1': 'value1 from x', 'key2': 'value2 from y', 'key3': 'value3 from y'}


# 2 --------------------------------------------------------------------------------------------------------------------
"""
    Assignment expressions:
    There is new syntax := that assigns values to variables as part of a larger expression.
    It is affectionately known as “the walrus operator”
"""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")


# 3 --------------------------------------------------------------------------------------------------------------------
"""
    Positional-only parameters:
    There is a new function parameter syntax / to indicate that some function parameters must be specified positionally
    and cannot be used as keyword arguments.
    
    In the following example, parameters a and b are positional-only, while c or d can be positional or keyword,
     and e or f are required to be keywords:
"""


def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)  # f(10, 20, 30, d=40, e=50, f=60)


# 4 --------------------------------------------------------------------------------------------------------------------
def parse(family):
    lastname, *members = family.split()  # lastname = first element, *members = rest of members.
    return lastname.upper(), *members


parse('simpsons homer marge bart lisa maggie')  # ('SIMPSONS', 'homer', 'marge', 'bart', 'lisa', 'maggie')
