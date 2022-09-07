# https://peps.python.org/pep-0525/
# https://www.programiz.com/python-programming/generator
"""
    Generators

    If a function contains at least one yield statement (it may contain other yield or return statements),
    it becomes a generator function. Both yield and return will return some value from a function.

    The difference is that while a return statement terminates a function entirely,
    yield statement pauses the function saving all its states and later continues from there on successive calls.
"""

""" 
    Differences between Generator function and Normal function:
    -> Generator function contains one or more yield statements.
    -> When called, it returns an object (iterator) but does not start execution immediately.
    -> Methods like __iter__() and __next__() are implemented automatically.
       So we can iterate through the items using next().
    
    ->
    -> Once the function yields, the function is paused and the control is transferred to the caller.
    -> Local variables and their states are remembered between successive calls.
    -> Finally, when the function terminates, StopIteration is raised automatically on further calls.
    
    Here is an example to illustrate all of the points stated above. 
    We have a generator function named my_gen() with several yield statements.
"""


# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


a = my_gen()

next(a)  # This is printed first
next(a)  # This is printed second
next(a)  # This is printed at last
# next(a)
# Traceback (most recent call last):
# ...
# StopIteration
# >>> next(a)
# Traceback (most recent call last):
# ...
# StopIteration


""" One final thing to note is that we can use generators with for loops directly. """


# A simple generator function
def my_gen():
    n = 1
    print(f'This is printed first - {n}')
    # Generator function contains yield statements
    yield n

    n += 1
    print(f'This is printed second - {n}')
    yield n

    n += 1
    print(f'This is printed at last - {n}')
    yield n


# Using for loop
for item in my_gen():
    print(item)
# 1
# This is printed second - 2
# 2
# This is printed at last - 3
# 3


""" Normally, generator functions are implemented with a loop having a suitable terminating condition. """


def rev_str(my_str):
    length = len(my_str)

    for i in range(length - 1, -1, -1):
        yield my_str[i]


# For loop to reverse the string
for char in rev_str("hello"):
    print(char)
# o
# l
# l
# e
# h


""" 
    Python Generator Expression
    
    Similar to the lambda functions which create anonymous functions, 
    generator expressions create anonymous generator functions.
    
    They have lazy execution ( producing items only when asked for ). 
    For this reason, a generator expression is much more memory efficient than an equivalent list comprehension.
"""
# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
list_ = [x ** 2 for x in my_list]

# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
generator = (x**2 for x in my_list)

print(list_)
print(generator)


""" 
    We can see above that the generator expression did not produce the required result immediately.
    Instead, it returned a generator object, which produces items only on demand.
    
    Here is how we can start getting items from the generator:
"""
# Initialize the list
my_list = [1, 3, 6, 10]

generator = (x ** 2 for x in my_list)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
# next(generator)
# Traceback (most recent call last):
#   File ".../python-complete-guide/python-3.10-docs/generator.py", line 148, in <module>
#     next(generator)
# StopIteration


""" Example """


def pow_two_gen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1


for value in pow_two_gen(max=1):
    print(value)

"""
    1. Easy to Implement
    2. Memory Efficient:
        A normal function to return a sequence will create the entire sequence in memory before returning the result. 
        This is an overkill, if the number of items in the sequence is very large.
        
        Generator implementation of such sequences is memory friendly and is preferred since it only produces
        one item at a time.
    
    3. Represent Infinite Stream
        Generators are excellent mediums to represent an infinite stream of data. 
        Infinite streams cannot be stored in memory, and since generators produce only one item at a time, 
        they can represent an infinite stream of data.

        The following generator function can generate all the even numbers (at least in theory).
    
    4. Pipelining Generators
        Multiple generators can be used to pipeline a series of operations.
    
    
"""

""" The following generator function can generate all the even numbers (at least in theory). """


def all_even():
    n = 0
    while True:
        yield n
        n += 2


"""
    Suppose we have a generator that produces the numbers in the Fibonacci series. 
    And we have another generator for squaring numbers.

    If we want to find out the sum of squares of numbers in the Fibonacci series, 
    we can do it in the following way by pipelining the output of generator functions together.
"""


def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x + y
        yield x


def square(nums):
    for num in nums:
        yield num**2


for num in fibonacci_numbers(10):
    print(num)

# print(sum(square(fibonacci_numbers(10))))  # 4895
