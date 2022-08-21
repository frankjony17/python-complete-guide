# https://www.programiz.com/python-programming/methods/dictionary/fromkeys
"""
    Dictionary fromkeys()

    fromkeys() Syntax:
        -> dict.fromkeys(alphabets,number)
    Here, alphabets and numbers are the key and value of the dictionary.

    fromkeys() Parameters:
        -> alphabets - are the keys that can be any iterables like string, set, list, etc.
        -> numbers (Optional) - are the values that can be of any type or any iterables like string, set, list, etc.
    Note: The same value is assigned to all the keys of the dictionary.

    fromkeys() Return Value:
        -> a new dictionary with the given sequence of keys and values.

    The fromkeys() method creates a dictionary from the given sequence of keys and values.
    Example:
"""
# keys for the dictionary
alphabets = {'a', 'b', 'c'}

# value for the dictionary
number = 1

# creates a dictionary with keys and values
dictionary = dict.fromkeys(alphabets, number)

print(dictionary)  # {'a': 1, 'c': 1, 'b': 1}


""" Example 1: Python Dictionary fromkeys() with Key and Value ------------------------------------------------------"""
# set of vowels
keys = {'a', 'e', 'i', 'o', 'u'}

# assign string to the value
value = 'vowel'

# creates a dictionary with keys and values
vowels = dict.fromkeys(keys, value)

print(vowels)  # {'a': 'vowel', 'u': 'vowel', 'e': 'vowel', 'i': 'vowel', 'o': 'vowel'}


""" Example 2: fromkeys() without Value -----------------------------------------------------------------------------"""
# list of numbers
keys = [1, 2, 4]

# creates a dictionary with keys only
numbers = dict.fromkeys(keys)

print(numbers)  # {1: None, 2: None, 4: None}


""" Example 3: fromkeys() To Create A Dictionary From Mutable Object ------------------------------------------------"""
# set of vowels
keys = {'a', 'e', 'i', 'o', 'u'}

# list of number
value = [1]

vowels = dict.fromkeys(keys, value)
print(vowels)  # {'a': [1], 'u': [1], 'o': [1], 'e': [1], 'i': [1]}

# updates the list value
value.append(2)

print(vowels)  # {'a': [1, 2], 'u': [1, 2], 'o': [1, 2], 'e': [1, 2], 'i': [1, 2]}


""" Dictionary comprehension for mutable objects -----------------------------------------------------------------------

    We can use dictionary comprehension and prevent updating the dictionary 
    when the mutable object (list, dictionary, etc) is updated.
    
    For example:
"""
# vowels keys
keys = {'a', 'e', 'i', 'o', 'u'}
value = [1]

# creates dictionary using dictionary comprehension
vowels = {key: list(value) for key in keys}

print(vowels)  # {'a': [1], 'u': [1], 'o': [1], 'e': [1], 'i': [1]}

# updates the value list
value.append(2)

print(vowels)  # {'a': [1], 'u': [1], 'o': [1], 'e': [1], 'i': [1]}
