"""
    List reverse()
    In this tutorial, we will learn about the Python List reverse() method with the help of examples.

    Syntax of List reverse()
        list.reverse()

    reverse() parameter
        The reverse() method doesn't take any arguments.

    Return Value from reverse()
        The reverse() method doesn't return any value.
        It updates the existing list.

    The reverse() method reverses the elements of the list.
    Example:
"""

# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]

# reverse the order of list elements
prime_numbers.reverse()


print('Reversed List:', prime_numbers)  # Reversed List: [7, 5, 3, 2]


""" Example 1: Reverse a List """
systems = ['Windows', 'macOS', 'Linux']

print('Original List:', systems)  # Original List: ['Windows', 'macOS', 'Linux']

# List Reverse
systems.reverse()

# updated list
print('Updated List:', systems)  # Updated List: ['Linux', 'macOS', 'Windows']


""" Example 2: Reverse a List Using Slicing Operator """
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)  # Original List: ['Windows', 'macOS', 'Linux']

# Reversing a list
# Syntax: reversed_list = systems[start:stop:step]
reversed_list = systems[::-1]

print('Updated List:', reversed_list)  # Updated List: ['Linux', 'macOS', 'Windows']


"""
    Example 3: Accessing Elements in Reversed Order
"""
# Operating System List
systems = ['Windows', 'macOS', 'Linux']

# Printing Elements in Reversed Order
for o in reversed(systems):
    print(o)

# Linux
# macOS
# Windows
