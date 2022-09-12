"""
    map()
    In this tutorial, we will learn about the Python map() function with the help of examples.

    map() Syntax:
        map(function, iterable, ...)

    map() Parameter:
        -> function - a function that perform some action to each element of an iterable
        -> iterable - an iterable like sets, lists, tuples, etc.
    You can pass more than one iterable to the map() function.

    map() Return Value:
        The map() function returns an object of map class.
        The returned value can be passed to functions like:
            -> list() - to convert to list
            -> set() - to convert to a set, and so on.

    The map() function applies a given function to each item of an iterable (list, tuple etc.)
    and returns an iterator.

    Example:
"""
numbers = [2, 4, 6, 8, 10]


# returns square of a number
def square(number):
    return number * number


# apply square() function to each item of the numbers list
squared_numbers_iterator = map(square, numbers)

# converting to list
squared_numbers = list(squared_numbers_iterator)
print(squared_numbers)  # [4, 16, 36, 64, 100]


""" Example 1: Working of map() ----------------------------------------------------------------"""


def calculate_square(n):
    return n * n


numbers = (1, 2, 3, 4)
result = map(calculate_square, numbers)
print(result)  # <map object at 0x7f722da129e8>

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)  # {16, 1, 4, 9}


""" Example 2: How to use lambda function with map() -------------------------------------------"""
numbers = (1, 2, 3, 4)

result = map(lambda x: x * x, numbers)

print(result)  # <map 0x7fafc21ccb00>

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)  # {16, 1, 4, 9}


""" Example 3: Passing Multiple Iterators to map() Using Lambda --------------------------------"""
num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lambda n1, n2: n1 + n2, num1, num2)

print(list(result))  # [9, 11, 13]
