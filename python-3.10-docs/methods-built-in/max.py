# https://www.programiz.com/python-programming/methods/built-in/max
"""
    The max() function returns the largest item in an iterable.
    It can also be used to find the largest item between two or more parameters.

    The max() function has two forms:
        -> max(iterable, *iterables, key, default)
        -> max(arg1, arg2, *args, key)

    max() with iterable arguments - max(iterable, *iterables, key, default):
        Parameters:
            -> iterable              - an iterable such as list, tuple, set, dictionary, etc.
            -> *iterables (optional) - any number of iterables; can be more than one
            -> key (optional)        - key function where the iterables are passed and comparison is performed
                                       based on its return value
            -> default (optional)    - default value if the given iterable is empty
        Return Value:
            ->  returns the largest element from an iterable.


"""
numbers = [9, 34, 11, -4, 27]

# find the maximum number
max_number = max(numbers)
print(max_number)  # 34

""" Example 1: Get the largest item in a list """
number = [3, 2, 8, 5, 10, 6]
largest_number = max(number);

print("The largest number is:", largest_number)  # The largest number is: 10

""" 
    Example 2: the largest string in a list
    
    If the items in an iterable are strings, the largest item (ordered alphabetically) is returned.
"""
languages = ["Python", "C Programming", "Java", "JavaScript"]
largest_string = max(languages)

print("The largest string is:", largest_string)  # The largest string is: Python

""" 
    Example 3: max() in dictionaries
    
    In the second max() function, we have passed a lambda function to the key parameter.
        -> key = lambda k: square[k]
    
    In the case of dictionaries, max() returns the largest key.
    Let's use the key parameter so that we can find the dictionary's key having the largest value.
"""
square = {2: 4, -3: 9, -1: 1, -2: 4}

# the largest key
key1 = max(square)
print("The largest key:", key1)  # 2

# the key whose value is the largest
key2 = max(square, key=lambda k: square[k])  # The key with the largest value: -3

print("The key with the largest value:", key2)  # -3
# getting the largest value
print("The largest value:", square[key2])  # 9


"""
    2. max() without iterable
    
    max() Syntax
    To find the largest object between two or more parameters, we can use this syntax:
        -> max(arg1, arg2, *args, key)
        
    max() parameters:
        -> arg1             - an object; can be numbers, strings, etc.
        -> arg2             - an object; can be numbers, strings, etc.
        -> *args (optional) - any number of objects
        -> key (optional)   - key function where each argument is passed, and comparison is performed based on its return value
    
        Basically, the max() function finds the largest item between two or more objects.
    
    max() Return Value
        max() returns the largest argument among the multiple arguments passed to it.
"""

""" Example 4: Find the maximum among the given numbers """
# find max among the arguments
result = max(4, -5, 23, 5)
print("The maximum number is:", result)  # The maximum number is: 23

