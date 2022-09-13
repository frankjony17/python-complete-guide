"""
  Use a nested list comprehension to find all of the numbers from 1-1000
  that are divisible by any single digit besides 1 (2-9)
"""

numbers = range(1, 1000)

divisible_numbers = [num for num in numbers if True in [True for n in range(2, 10) if num % n == 0]]

print("Have ", len(divisible_numbers), "numbers, divisible by a digit.")
print(divisible_numbers)
