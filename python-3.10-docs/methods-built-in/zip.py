# https://www.programiz.com/python-programming/methods/built-in/zip
"""
    zip()
    The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.

    The syntax of the zip() function is:
        -> zip(*iterables)

    zip() Parameters:
        -> Parameter	Description
        -> iterables	can be built-in iterables (like: list, string, dict), or user-defined iterables
    Recommended Reading: Python Iterators, __iter__ and __next__

    zip() Return Value:
    The zip() function returns an iterator of tuples based on the iterable objects.
        -> If we do not pass any parameter, zip() returns an empty iterator
        -> If a single iterable is passed, zip() returns an iterator of tuples with each tuple having only one element.
        -> If multiple iterables are passed,
           zip() returns an iterator of tuples with each tuple having elements from all the iterables.

        Suppose, two iterables are passed to zip(); one iterable containing three and other containing five elements.
        Then, the returned iterator will contain three tuples.
        It's because the iterator stops when the shortest iterable is exhausted.
"""
languages = ['Java', 'Python', 'JavaScript']
versions = [14, 3, 6]

result = zip(languages, versions)
print(list(result))  # [('Java', 14), ('Python', 3), ('JavaScript', 6)]


""" Example 1: Python zip() """
number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']

# No iterables are passed
result = zip()

# Converting iterator to list
result_list = list(result)
print(result_list)  # []

# Two iterables are passed
result = zip(number_list, str_list)

# Converting iterator to set
result_set = set(result)
print(result_set)  # {(2, 'two'), (3, 'three'), (1, 'one')}


""" Example 2: Different number of iterable elements """
numbersList = [1, 2, 3]
str_list = ['one', 'two']
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')

# Notice, the size of numbersList and numbers_tuple is different
result = zip(numbersList, numbers_tuple)

# Converting to set
result_set = set(result)
print(result_set)  # {(2, 'TWO'), (3, 'THREE'), (1, 'ONE')}

result = zip(numbersList, str_list, numbers_tuple)

# Converting to set
result_set = set(result)
print(result_set)  # {(2, 'two', 'TWO'), (1, 'one', 'ONE')}


"""
    The * operator can be used in conjunction with zip() to unzip the list.
        -> zip(*zippedList)
    
    Example 3: Unzipping the Value Using zip()
"""
coordinate = ['x', 'y', 'z']
value = [3, 4, 5]

result = zip(coordinate, value)
result_list = list(result)
print(result_list)  # [('x', 3), ('y', 4), ('z', 5)]

c, v = zip(*result_list)
print('c =', c)  # c = ('x', 'y', 'z')
print('v =', v)  # v = (3, 4, 5)
