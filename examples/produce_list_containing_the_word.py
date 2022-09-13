"""
  Given numbers = range(20),
  produce a list containing the word
    "even" if a number in the numbers is even,
    and the word
    "odd" if the number is odd.

    Result would look like ‘odd’, ’odd’, ‘even’

    Note:
      An even number is a number that can be divided into two equal groups.
      An odd number is a number that cannot be divided into two equal groups.
      Even numbers end in 2, 4, 6, 8 and 0 regardless of how many digits they have
      (we know the number 5,917,624 is even because it ends in a 4!).
      Odd numbers end in 1, 3, 5, 7, 9.
"""

numbers = range(20)

words = ["even" if num % 2 == 0 else "odd" for num in numbers]

print(words)
