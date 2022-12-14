# https://www.programiz.com/python-programming/dictionary-comprehension

"""
    Dictionary Comprehension.
    Dictionary comprehension is an elegant and concise way to create dictionaries.

    Using Dictionary Comprehension:
        -> dictionary = {key: value for vars in iterable}


    Example 1: Dictionary Comprehension
    Consider the following code:
"""

square_dict = dict()

for num in range(1, 11):
    square_dict[num] = num * num

print(square_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


""" Now, let's create the dictionary in the above program using dictionary comprehension -------"""
# dictionary comprehension example
square_dict = {num: num * num for num in range(1, 11)}
print(square_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


""" Example 3: How to use Dictionary Comprehension ---------------------------------------------"""
# item price in dollars
old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}

dollar_to_pound = 0.76

new_price = {item: value * dollar_to_pound for (item, value) in old_price.items()}

print(new_price)  # {'milk': 0.7752, 'coffee': 1.9, 'bread': 1.9}


""" Example 4: If Conditional Dictionary Comprehension -----------------------------------------"""
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

even_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0}

print(even_dict)  # {'jack': 38, 'michael': 48}


""" Example 5: Multiple if Conditional Dictionary Comprehension --------------------------------"""
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

new_dict = {k: v for (k, v) in original_dict.items() if v % 2 != 0 if v < 40}

print(new_dict)  # {'john': 33}


""" Example 6: if-else Conditional Dictionary Comprehension ------------------------------------"""
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

new_dict_1 = {k: ('old' if v > 40 else 'young') for (k, v) in original_dict.items()}

print(new_dict_1)  # {'jack': 'young', 'michael': 'old', 'guido': 'old', 'john': 'young'}


""" Example 7: Nested Dictionary with Two Dictionary Comprehensions ----------------------------"""
dictionary = {k1: {k2: k1 * k2 for k2 in range(1, 6)} for k1 in range(2, 5)}

print(dictionary)
# {
#     2: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10},
#     3: {1: 3, 2: 6, 3: 9, 4: 12, 5: 15},
#     4: {1: 4, 2: 8, 3: 12, 4: 16, 5: 20}
# }
