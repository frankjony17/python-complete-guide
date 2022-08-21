# https://www.programiz.com/python-programming/methods/dictionary/copy
"""
    Dictionary copy()

    They copy() method returns a copy (shallow copy) of the dictionary.

    The syntax of copy() is:
        -> dict.copy()

    copy() Arguments (doesn't take any arguments):

    copy() Return Value
        This method returns a shallow copy of the dictionary.
        It doesn't modify the original dictionary.

    Example:
"""
original_marks = {'Physics': 67, 'Maths': 87}

copied_marks = original_marks.copy()


print('Original Marks:', original_marks)  # Original Marks: {'Physics': 67, 'Maths': 87}
print('Copied Marks:', copied_marks)  # {'Physics': 67, 'Maths': 87}


""" Example 1: How copy works for dictionaries? ---------------------------------------------------------------------"""
original = {1: 'one', 2: 'two'}
new = original.copy()

print('Orignal: ', original)  # {1: 'one', 2: 'two'}
print('New: ', new)  # {1: 'one', 2: 'two'}


""" Dictionary copy() Method Vs = Operator -----------------------------------------------------------------------------

    When the copy() method is used, 
    a new dictionary is created which is filled with a copy of the references from the original dictionary.
    
    When the = operator is used, a new reference to the original dictionary is created.
"""
original = {1: 'one', 2: 'two'}
new = original

# removing all elements from the dictionary
new.clear()

print('new: ', new)  # {}
print('original: ', original)  # {}


""" Example 3: Using copy() to Copy Dictionaries --------------------------------------------------------------------"""
original = {1: 'one', 2: 'two'}
new = original.copy()

# removing all elements from the list
new.clear()

print('new: ', new)  # {}
print('original: ', original)  # {1: 'one', 2: 'two'}
