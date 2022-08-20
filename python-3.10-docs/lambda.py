from x_utils import expression
# https://www.pythontutorial.net/python-basics/python-lambda-expressions/
"""
    What are Python lambda expressions:
    Python lambda expressions allow you to define anonymous functions.

    Anonymous functions are functions without names.
    The anonymous functions are useful when you need to use them once.
    A lambda expression typically contains one or more arguments, but it can have only one expression.

    The following shows the lambda expression syntax:
"""

# lambda parameters: expression

"""It’s equivalent to the following function without the "anonymous" name:"""


def anonymous(parameters):
    return expression


# 1 --------------------------------------------------------------------------------------------------------------------
def get_full_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)


full_name_1 = get_full_name(
    'John',
    'Doe',
    lambda first_name, last_name: f"{first_name} {last_name}"
)

full_name_2 = get_full_name(
    'John',
    'Doe',
    lambda first_name, last_name: f"{last_name} {first_name}"
)

print(full_name_1)  # John Doe
print(full_name_2)  # Doe, John


# 2 --------------------------------------------------------------------------------------------------------------------
sum_values = lambda x: x + 5

value = sum_values(10)
print(value)


# 3 --------------------------------------------------------------------------------------------------------------------
praices = [125, 250, 17, 84]

taxes = list(map(lambda x: x * 0.4, praices))

print(taxes)  # [50.0, 100.0, 6.800000000000001, 33.6]


# 4 --------------------------------------------------------------------------------------------------------------------
""" Program to filter out only the even items from a list (pair numbers)"""
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x % 2 == 0), my_list))

print(new_list)


# 5 --------------------------------------------------------------------------------------------------------------------
""" Program to double each item in a list using map() """
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2, my_list))

print(new_list)
