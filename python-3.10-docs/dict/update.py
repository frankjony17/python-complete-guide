# https://www.programiz.com/python-programming/methods/dictionary/update
"""
    Dictionary update()

    Syntax of Dictionary update():
        -> dict.update([other])

    update() Parameters:
        -> The update() method takes either a dictionary or an iterable object of key/value pairs (generally tuples).
        -> If update() is called without passing parameters, the dictionary remains unchanged.

    Return Value from update()
        -> update() method updates the dictionary with elements from a dictionary
                    object or an iterable object of key/value pairs.
        -> It doesn't return any value (returns None).

    The update() method updates the dictionary with the elements from another dictionary
     object or from an iterable of key/value pairs.

    Example:
"""
marks = {'Physics': 67, 'Maths': 87}
internal_marks = {'Practical': 48}

marks.update(internal_marks)

print(marks)  # {'Physics': 67, 'Maths': 87, 'Practical': 48}


""" Example 1: Working of update() """
dict_1 = {1: "one", 2: "three"}
dict_2 = {2: "two"}

# updates the value of key 2
dict_1.update(dict_2)
print(dict_1)

dict_2 = {3: "three"}

# adds element with key 3
dict_1.update(dict_2)
print(dict_1)


""" Example 2: update() When Tuple is Passed """
dictionary = {'x': 2}

dictionary.update([('y', 3), ('z', 0)])

print(dictionary)  # {'x': 2, 'y': 3, 'z': 0}

