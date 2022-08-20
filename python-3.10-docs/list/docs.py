# https://www.programiz.com/python-programming/list
# https://www.pythontutorial.net/python-basics/python-list/

"""
    append()	adds an element to the end of the list
    extend()	adds all elements of a list to another list
    insert()	inserts an item at the defined index
    remove()	removes an item from the list
    pop()	    returns and removes an element at the given index
    clear()	    removes all items from the list
    index()	    returns the index of the first matched item
    count()	    returns the count of the number of items passed as an argument
    sort()	    sort items in a list in ascending order
    reverse()	reverse the order of items in the list
    copy() 	    returns a shallow copy of the list
"""

""" 1 -- append --------------------------------------------------------------------------------------------------------

    Adding elements to the list.
"""
numbers = [1, 3, 2, 7, 9, 4]

numbers.append(100)

print(numbers)  # [1, 3, 2, 7, 9, 4, 100]


""" 2 -- insert -- [2:2] = [5, 7] --------------------------------------------------------------------------------------

    The insert() method adds a new element at any position in the list.
"""
numbers = [1, 3, 2, 7, 9, 4]

numbers.insert(2, 100)

print(numbers)  # [1, 3, 100, 2, 7, 9, 4]

# insert multiple items by squeezing it into an empty slice of a list.
numbers[2:2] = [5, 7]

print(numbers)  # [1, 3, 5, 7, 100, 2, 7, 9, 4]


""" 3 -- del -- [1:3] --------------------------------------------------------------------------------------------------
    
    Removing elements from a list
"""
numbers = [1, 3, 2, 7, 9, 4]
del numbers[0]

print(numbers)  # [3, 2, 7, 9, 4]

# delete multiple items
del numbers[1:3]

print(numbers)  # [3, 9, 4]

# delete the entire list
del numbers

# Error: List not defined
# print(numbers)  -> NameError: name 'numbers' is not defined


""" 4 -- pop -----------------------------------------------------------------------------------------------------------

   The pop() method removes the last element from a list and returns that element:
"""
numbers = [1, 3, 2, 7, 9, 4]
last = numbers.pop()

print(last)  # 4
print(numbers)  # [1, 3, 2, 7, 9]

# To pop an element by its position, you use the pop() with the element’s index.
# For example:

numbers = [1, 3, 2, 7, 9, 4]

second = numbers.pop(1)

print(second)  # 3
print(numbers)  # [1, 2, 7, 9, 4]


""" 5 -- remove --------------------------------------------------------------------------------------------------------

    To remove an element by value, you use the remove() method.
    For example, the following removes the element with value 9 from the numbers list:
    Remove the first element!
"""
numbers = [1, 3, 2, 7, 9, 4, 9]

numbers.remove(9)
print(numbers)  # [1, 3, 2, 7, 4, 9]


""" 6 -- Slicing -- [:] ------------------------------------------------------------------------------------------------

    List Slicing in Python.
    We can access a range of items in a list by using the slicing operator : .
"""
# List slicing in Python
my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']

# elements from index 2 to index 4
print(my_list[2:5])  # ['o', 'g', 'r']

# elements from index 5 to end
print(my_list[5:])  # ['a', 'm', 'i', 'z']

# elements from index 0 to 5
print(my_list[:5])  # ['p', 'r', 'o', 'g', 'r']

# elements beginning to end
print(my_list[:])  # ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']


""" 7 -- Add/Change -- [1:4] = [3, 5, 7] -------------------------------------------------------------------------------
    
    Add/Change List Elements.
    Lists are mutable, meaning their elements can be changed unlike string or tuple.
"""
# Correcting mistake values in a list
odd = [2, 4, 6, 8]

# change the 1st item
odd[0] = 1

print(odd)  # [1, 4, 6, 8]

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]

print(odd)  # [1, 3, 5, 7]


""" 8 -- extend --------------------------------------------------------------------------------------------------------
    
    Add several items using the extend() method.
"""
odd = [1, 3, 5, 7]

odd.extend([9, 11, 13])

print(odd)  # [1, 3, 5, 7, 9, 11, 13]


""" 9 -- [1] + [2] = [1, 2] -- [5] * 3 = [5, 5, 5] ---------------------------------------------------------------------
    
    We can also use + operator to combine two lists.
    This is also called concatenation.
"""
# Concatenating and repeating lists
odd = [1, 3, 5]

print(odd + [9, 7, 5])  # [1, 3, 5, 9, 7, 5]

# The * operator repeats a list for the given number of times.
print(["re"] * 3)  # ['re', 're', 're']


""" 10 -- clear --------------------------------------------------------------------------------------------------------

    If we have to empty the whole list, we can use the clear() method.
"""
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

my_list.clear()

# Output: []
print(my_list)  # []


""" 11 -- Delete -- [2:3] = [] -----------------------------------------------------------------------------------------

    Delete items in a list by assigning an empty list to a slice of elements.
"""
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
my_list[2:3] = []

print(my_list)  # ['p', 'r', 'b', 'l', 'e', 'm']

my_list[2:5] = []

print(my_list)  # ['p', 'r', 'm']


""" 12 -- index --------------------------------------------------------------------------------------------------------

    The index() method returns the index of the specified element in the list.
    The syntax of the list index() method is:
        
        list.index(element, start, end)
    
    The list index() method can take a maximum of three arguments:
        element - the element to be searched
        start (optional) - start searching from this index
        end (optional) - search the element up to this index
"""

animals = ['cat', 'dog', 'rabbit', 'horse']

# get the index of 'dog'
index = animals.index('dog')

print(index)  # Output: 1

# If not find the element raise an exception: ValueError: 'element' is not in list


""" 13 -- count --------------------------------------------------------------------------------------------------------
    The count() method returns the number of times the specified element appears in the list.
    
    The syntax of the count() method is:
        list.count(element)
"""

# create a list
numbers = [2, 3, 5, 2, 11, 2, 7]

# check the count of 2
count = numbers.count(2)

print('Count of 2:', count)  # Output: Count of 2: 3




