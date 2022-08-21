# https://www.programiz.com/python-programming/methods/dictionary
"""
    Dictionary
    Creating Python Dictionary
    Creating a dictionary is as simple as placing items inside curly braces {} separated by commas.

    An item has a key and a corresponding value that is expressed as a pair (key: value).

    While the values can be of any data type and can repeat,
    keys must be of immutable type (string, number or tuple with immutable elements) and must be unique.
"""
# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}  # {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}  # {'name': 'John', 1: [2, 4, 3]}

# using dict()
my_dict = dict({1: 'apple', 2: 'ball'})  # {'name': 'John', 1: [2, 4, 3]}

# from sequence having each item as a pair
my_dict = dict([(1, 'apple'), (2, 'ball')])  # {1: 'apple', 2: 'ball'}


""" Accessing Elements from Dictionary ------------------------------------------------------------------------------"""
# get vs [] for retrieving elements
my_dict = {'name': 'Jack', 'age': 26}

print(my_dict['name'])  # Jack
print(my_dict.get('age'))  # 26

# Trying to access keys which doesn't exist throws error
print(my_dict.get('address'))  # None

# KeyError
print(my_dict['address'])  # KeyError: 'address'


""" Changing and Adding Dictionary elements -------------------------------------------------------------------------"""
# Changing and adding Dictionary Elements
my_dict = {'name': 'Jack', 'age': 26}

# update value
my_dict['age'] = 27
print(my_dict)  # {'age': 27, 'name': 'Jack'}

# add item
my_dict['address'] = 'Downtown'
print(my_dict)  # {'address': 'Downtown', 'age': 27, 'name': 'Jack'}


""" Removing elements from Dictionary -- pop -- popitem -- clear -- del -- pop -- popitem -- clear -- del -- pop ----"""
# create a dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

""" Remove a particular item, returns its value """
print(squares.pop(4))  # 16
print(squares)  # {1: 1, 2: 4, 3: 9, 5: 25}

""" Removes and returns the last element (key,value) """
print(squares.popitem())  # (5, 25)
print(squares)  # Output: {1: 1, 2: 4, 3: 9}

""" Remove all items """
squares.clear()
print(squares)  # {}

""" Delete the dictionary itself """
del squares

# Throws Error
# print(squares)  # NameError: name 'squares' is not defined

""" -- setdefault -- setdefault -- setdefault -- setdefault -- setdefault -- setdefault -- setdefault -- setdefault ----
    
    The setdefault() method returns the value of a key (if the key is in dictionary). 
    If not, it inserts key with a value to the dictionary.
    
    Dictionary setdefault()
        -> dict.setdefault(key[, default_value])
    
    setdefault() Parameters:
        -> key - the key to be searched in the dictionary
        -> default_value (optional) - key with a value default_value is inserted to the dictionary 
                                      if the key is not in the dictionary.
           
    If not provided, the default_value will be None.
    
    Return Value from setdefault():
        -> value of the key if it is in the dictionary
        -> None if the key is not in the dictionary and default_value is not specified
        -> default_value if key is not in the dictionary and default_value is specified

"""

""" Example 1: How setdefault() works when key is in the dictionary? """
person = {'name': 'Phill', 'age': 22}

age = person.setdefault('age')

print('person = ', person)  # person =  {'name': 'Phill', 'age': 22}
print('Age = ', age)  # Age = 22


""" Example 2: How setdefault() works when key is not in the dictionary? """
person = {'name': 'Phill'}

# key is not in the dictionary
salary = person.setdefault('salary')

print('person = ', person)  # person =  {'name': 'Phill', 'salary': None}
print('salary = ', salary)  # salary =  None

# key is not in the dictionary, default_value is provided
age = person.setdefault('age', 22)
print('person = ', person)  # person =  {'name': 'Phill', 'age': 22, 'salary': None}
print('age = ', age)  # age =  22

"""
    Python Dictionary Methods
    Methods that are available with a dictionary are tabulated below. 
    Some of them have already been used in the above examples.
    
    Method	Description
        clear()	            -> Removes all items from the dictionary.
        copy()	            -> Returns a shallow copy of the dictionary.
        fromkeys(seq[, v])	-> Returns a new dictionary with keys from seq and value equal to v (defaults to None).
        get(key[,d])	    -> Returns the value of the key. If the key does not exist, returns d (defaults to None).
        items()	            -> Return a new object of the dictionary's items in (key, value) format.
        keys()	            -> Returns a new object of the dictionary's keys.
        pop(key[,d])	    -> Removes the item with the key and returns its value or d if key is not found.
                               If d is not provided and the key is not found, it raises KeyError.
        popitem()	        -> Removes and returns an arbitrary item (key, value).
                               Raises KeyError if the dictionary is empty.
        setdefault(key[,d])	-> Returns the corresponding value if the key is in the dictionary.
                               If not, inserts the key with a value of d and returns d (defaults to None).
        update([other])	    -> Updates the dictionary with the key/value pairs from other, overwriting existing keys.
        values()	        -> Returns a new object of the dictionary's values
"""