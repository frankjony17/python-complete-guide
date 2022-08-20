# https://www.programiz.com/python-programming/methods/list/sort
""" -- sort ------------------------------------------------------------------------------------------------------------

    The sort() method sorts the items of a list in ascending or descending order.
    The syntax of the sort() method is:
        list.sort(key=..., reverse=...)

    Alternatively, you can also use Python's built-in sorted() function for the same purpose.
        sorted(list, key=..., reverse=...)

    sort() Parameters:
        -> reverse - If True, the sorted list is reversed (or sorted in Descending order)
        -> key - function that serves as a key for the sort comparison
"""

prime_numbers = [11, 3, 7, 5, 2]

# sorting the list in ascending order
prime_numbers.sort()

print(prime_numbers)  # [2, 3, 5, 7, 11]


"""
    Sort with custom function using key:
        list.sort(key=len)
        sorted(list, key=len)

    Here, len is Python's in-built function to count the length of an element.
    
    Example 3: Sort the list using key: 
"""


def take_second(elem):  # take second element for sort
    return elem[1]


# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
random.sort(key=take_second)

print('Sorted list:', random)  # Sorted list: [(4, 1), (2, 2), (1, 3), (3, 4)]


"""
    Suppose we have a list of information about the employees of an office where each element is a dictionary.

    We can sort the list in the following way:
"""
# sorting using custom key
employees = [
    {'name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]


# custom functions to get employee info
def get_name(employee):
    return employee.get('name')


def get_age(employee):
    return employee.get('age')


def get_salary(employee):
    return employee.get('salary')


# sort by name (Ascending order)
employees.sort(key=get_name)
print(employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=get_age)
print(employees, end='\n\n')

# sort by salary (Descending order)
employees.sort(key=get_salary, reverse=True)
print(employees, end='\n\n')


"""
    It is a good practice to use the lambda function when the function can be summarized in one line.
    So, we can also write the above program as:
"""
# sorting using custom key
employees = [
    {'name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

# sort by name (Ascending order)
employees.sort(key=lambda x: x.get('name'))
print(employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=lambda x: x.get('age'))
print(employees, end='\n\n')

# sort by salary (Descending order)
employees.sort(key=lambda x: x.get('salary'), reverse=True)
print(employees, end='\n\n')
