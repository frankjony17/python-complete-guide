"""
  Get only the numbers in a sentence like:
    "In 1984 there were 13 instances of a protest with over 1000 people attending"
"""

sentence = "In 1984 there were 13 instances of a protest with over 1000 people attending"

# Approach 1
numbers_1 = set([int(num) for num in sentence if num in '0123456789'])

# Approach 2
numbers_2 = [num for num in sentence.split() if not num.isalpha()]

print(numbers_1)
print(numbers_2)
