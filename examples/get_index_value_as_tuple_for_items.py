"""
  Get the index and the value as a tuple for items in the list
  “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’).

  Result would look like (index, value), (index, value)
"""
items = ["hi", 4, 8.99, "apple", ("t,b", "n")]

result_list = [(index, value) for index, value in enumerate(items)]

result_dict = {index: value for index, value in enumerate(items)}

print(result_list)
print(result_dict)
