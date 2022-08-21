# https://www.programiz.com/python-programming/methods/built-in/all

"""
    The all() function returns True if all elements in the given iterable are true.
    If not, it returns False.

    The syntax of the all() function is:
        -> all(iterable)

    The all() function takes a single parameter:
        -> iterable - any iterable (list, tuple, dictionary, etc.) which contains the elements

    all() function returns:
        -> True - If all elements in an iterable are true
        -> False - If any element in an iterable is false

    When	                                Return Value
    All values are true.	                True
    All values are false.	                False
    One value is true (others are false).	False
    One value is false (others are true).	False
    Empty Iterable.	                        True

    Example:
"""
boolean_list = ['True', 'True', 'True']

# check if all elements are true
result = all(boolean_list)

print(result)  # True


""" Example 1: How all() works for lists? """
# all values true
l = [1, 3, 4, 5]
print(all(l))  # True

# all values false
l = [0, False]
print(all(l))  # False

# one false value
l = [1, 3, 4, 0]
print(all(l))  # False

# one true value
l = [0, False, 5]
print(all(l))  # False

# empty iterable
l = []
print(all(l))  # True


""" Example 2: How all() works for strings? """
s = "This is good"
print(all(s))  # True

# 0 is False
# '0' is True
s = '000'
print(all(s))  # True

s = ''
print(all(s))  # True


""" 
    Example 3: How all() works with Python dictionaries? 
    
    In the case of dictionaries, if all keys (not values) are true or the dictionary is empty,
    all() returns True. Else, it returns false for all other cases.
"""
s = {0: 'False', 1: 'False'}
print(all(s))  # False

s = {1: 'True', 2: 'True'}
print(all(s))  # True

s = {1: 'True', False: 0}
print(all(s))  # False

s = {}
print(all(s))  # True

# 0 is False
# '0' is True
s = {'0': 'True'}
print(all(s))  # True
