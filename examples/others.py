
""" Example 1 """

x = "key1:value1 key2:value2 key3:value3"

to_dict = lambda string: [{"key": k, "value": v} for k, v in (s.split(":") for s in string.split())]
print(to_dict(x))
# [{'key': 'key1', 'value': 'value1'}, {'key': 'key2', 'value': 'value2'}, {'key': 'key3', 'value': 'value3'}]

to_dict = [{'key': x.split(':')[0], 'value':x.split(':')[1]} for x in x.split()]
print(to_dict)
# [{'key': 'key1', 'value': 'value1'}, {'key': 'key2', 'value': 'value2'}, {'key': 'key3', 'value': 'value3'}]


""" Example 2 
    
    Create a dictionary with all values multiplied by 2.
    Using 3 o more dictionaries for create a new one.
    
    dict_1 = {'d1a': 1, 'd1b': 2}
    dict_2 = {'d2a': 2, 'd2b': 3}
    dict_3 = {'d3c': 2, 'd3d': 4}

    Expected result:
        -> {'d1a': 2, 'd1b': 4, 'd2a': 4, 'd2b': 6, 'd3c': 4, 'd3d': 8}
"""
dict_1 = {'d1a': 1, 'd1b': 2}
dict_2 = {'d2a': 2, 'd2b': 3}
dict_3 = {'d3c': 2, 'd3d': 4}

dictionary_1 = {k: v * 2 for k, v in {**dict_1, **dict_2, **dict_3}.items()}

# Best way to do it
dictionary_2 = {k: v * 2 for k, v in (dict_1 | dict_2 | dict_3).items()}

print(dictionary_1)  # {'d1a': 2, 'd1b': 4, 'd2a': 4, 'd2b': 6, 'd3c': 4, 'd3d': 8}
print(dictionary_2)  # {'d1a': 2, 'd1b': 4, 'd2a': 4, 'd2b': 6, 'd3c': 4, 'd3d': 8}

""" Dictionary Comprehensions and merge dict with Union Operator"""

# ----------------------------------------------------------------------------------------------------------------------

""" Example 3
    Fibonacci Sequence
"""


def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x + y
        yield x

# ----------------------------------------------------------------------------------------------------------------------

# React: virtualenv
# Docker: run, cmd
# kafka: two services,
# send de message to one API and save something in database and them send de same message to another service
# or get the data from the database whith the id?
# alembic: migration how add new column and dta for this column
# redoc: perhaps react -> redoc
# python grafql
# Python statement.


"""
    Basic python data structure:
        https://realpython.com/python-data-structures/#dictionaries-maps-and-hash-tables
        https://docs.python.org/3/library/collections.html?highlight=collections#module-collections
   
    create a widget for a dashboard thats run on docker using react in frontend and django in backend
    React and Django   
    make a dashboard with react and django
    React + Python coding challenge
    
    Flatten it to the given specifications:
        https://www.programiz.com/python-programming/examples/flatten-nested-list
    
  
    What kind of software development are you interested in working on?
    
    Create a function that flattens a nested dictionary
    
    JUnit test cases
"""

