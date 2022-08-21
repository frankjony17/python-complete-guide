# https://www.programiz.com/python-programming/methods/built-in/iter

"""
    The iter() method returns an iterator for the given argument.

    The syntax of the iter() method is:
        -> iter(object, sentinel [optional])

    The iter() method takes two parameters:
        -> object              - can be a list, set, tuple, etc.
        -> sentinel [optional] - a special value that is used to represent the end of a sequence

    The iter() method returns:
        -> iterator object for the given argument until the sentinel character is found
        -> TypeError for a user-defined object that doesn't implement __iter__(), and __next__() or __getitem()__
"""

# list of vowels
phones = ['apple', 'samsung', 'oneplus']
phones_iter = iter(phones)

print(next(phones_iter))
print(next(phones_iter))
print(next(phones_iter))

# Output:
#   apple
#   samsung
#   oneplus


""" Example 1: Python iter() """
# list of vowels
vowels = ["a", "e", "i", "o", "u"]

# iter() with a list of vowels
vowels_iter = iter(vowels)

print(next(vowels_iter))  # a
print(next(vowels_iter))  # e
print(next(vowels_iter))  # i
print(next(vowels_iter))  # o
print(next(vowels_iter))  # u


""" Example 2: iter() for custom objects """


class PrintNumber:
    def __init__(self, max):
        self.max = max

    # iter() method in a class
    def __iter__(self):
        self.num = 0
        return self

    # next() method in a class
    def __next__(self):
        if (self.num >= self.max):
            raise StopIteration
        self.num += 1
        return self.num


print_num = PrintNumber(3)

print_num_iter = iter(print_num)
print(next(print_num_iter))  # 1
print(next(print_num_iter))  # 2
print(next(print_num_iter))  # 3

# raises StopIteration
print(next(print_num_iter))

# Output:
#   1
#   2
#   3
#   Traceback (most recent call last):
#      File "", line 23, in
#    File "", line 11, in __next__
#    StopIteration


""" Example 3: iter() with Sentinel Parameter """


class DoubleIt:
    def __init__(self):
        self.start = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.start *= 2
        return self.start

    __call__ = __next__


my_iter = iter(DoubleIt(), 16)

for x in my_iter:
    print(x)

# Output:
#   2
#   4
#   8
