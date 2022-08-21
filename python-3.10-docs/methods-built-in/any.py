# https://www.programiz.com/python-programming/methods/built-in/any
"""
    any()

    The syntax of any() is:
        -> any(iterable)

    any() Parameters
        -> The any() function takes an iterable (list, string, dictionary etc.) in Python.

    any() Return Value:
        -> True  - if at least one element of an iterable is true
        -> False - if all elements are false or if an iterable is empty

    Condition	                            Return Value
    All values are true.	                True
    All values are false.	                False
    One value is true (others are false).	True
    One value is false (others are true).	True
    Empty Iterable.	                        False

    The any() function returns True if any element of an iterable is True.
    If not, it returns False.
"""
boolean_list = ['True', 'False', 'True']

# check if any element is true
result = any(boolean_list)
print(result)  # True


""" Example 1: Using any() on Python Lists """
# True since 1,3 and 4 (at least one) is true
l = [1, 3, 4, 0]
print(any(l))  # True

# False since both are False
l = [0, False]
print(any(l))  # False

# True since 5 is true
l = [0, False, 5]
print(any(l))  # True

# False since iterable is empty
l = []
print(any(l))  # False


""" Example 2: Using any() on Python Strings """
# At east one (in fact all) elements are True
s = "This is good"
print(any(s))  # True

# 0 is False
# '0' is True since its a string character
s = '000'
print(any(s))  # True

# False since empty iterable
s = ''
print(any(s))  # False


""" Example 3: Using any() with Python Dictionaries """
# 0 is False
d = {0: 'False'}
print(any(d))  # False

# 1 is True
d = {0: 'False', 1: 'True'}
print(any(d))  # True

# 0 and False are false
d = {0: 'False', False: 0}
print(any(d))  # False

# iterable is empty
d = {}
print(any(d))  # False

# 0 is False
# '0' is True
d = {'0': 'False'}
print(any(d))  # False
