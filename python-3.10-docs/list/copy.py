# https://www.programiz.com/python-programming/methods/list/copy
"""
    List copy()

    In this tutorial, we will learn about the Python List copy() method with the help of examples.

    copy() Syntax
    The syntax of the copy() method is:
        new_list = list.copy()

    copy() Parameters
        The copy() method doesn't take any parameters.

    The copy() method returns a shallow copy of the list.
"""

# mixed list
prime_numbers = [2, 3, 5]

# copying a list
numbers = prime_numbers.copy()


print('Copied List:', numbers)  # Copied List: [2, 3, 5]


"""
    List copy using =
    We can also use the = operator to copy a list. 
    For example:
"""
old_list = [1, 2, 3]
new_list = old_list

"""
    Howerver, there is one problem with copying lists in this way. 
    If you modify new_list, old_list is also modified.
    It is because the new list is referencing or pointing to the same old_list object.
"""
old_list = [1, 2, 3]

# copy list using =
new_list_1 = old_list


# add an element to list
new_list_1.append('a')

print('New List:', new_list)  # New List: [1, 2, 3, 'a']
print('Old List:', old_list)  # Old List: [1, 2, 3, 'a']


"""
     Copy List Using Slicing Syntax
"""
# shallow copy using the slicing syntax

# mixed list
list_1 = ['cat', 0, 6.7]

# copying a list using slicing
new_list = list_1[:]

# Adding an element to the new list
new_list.append('dog')

# Printing new and old list
print('Old List:', list_1)  # Old List: ['cat', 0, 6.7]
print('New List:', new_list)  # New List: ['cat', 0, 6.7, 'dog']

