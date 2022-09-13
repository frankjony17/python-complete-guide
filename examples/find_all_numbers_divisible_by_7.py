"""
  Find all of the numbers from 1-1000 that are divisible by 7
"""
numbers = [num for num in range(1, 1001) if num % 7 == 0]

print("There are ", len(numbers), " numbrers divisible by 7: \n", numbers)
