"""
  Produce a list of tuples consisting of only the matching numbers in these lists:
  list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  list_b = [2, 7, 1, 12]

  Result would look like (4,4), (12,12)
"""

list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_b = [2, 7, 1, 12]

# Approach 1
list_of_tuples_1 = [(num, num) for num in list_a if num in list_b]

# Approach 2
list_of_tuples_2 = [(a, b) for a in list_a for b in list_b if a == b]

print(list_of_tuples_1)
print(list_of_tuples_2)
