# Use for the questions below:

nums = [i for i in range(1, 1001)]

string = "Practice Problems to Drill List Comprehension in Your Head."

"""
    1. Find all of the numbers from 1–1000 that are divisible by 8
"""
q1_answer = [num for num in nums if num % 8 == 0]

print(q1_answer)

"""
    2. Find all of the numbers from 1–1000 that have a 6 in them
"""
q2_answer = [num for num in nums if "6" in str(num)]

"""
    3. Count the number of spaces in a string
"""
q3_answer = len([char for char in string if char == " "])

"""
    4. Remove all of the vowels in a string
"""
q4_answer = "".join([char for char in string if char not in ["a", "e", "i", "o", "u"]])
print(q4_answer)


"""
    5. Find all of the words in a string that are less than 5 letters
"""
words = string.split()
q5_answer = [word for word in words if len(word) < 5]


"""
    6. Use a dictionary comprehension to count the length of each word in a sentence
"""
q6_answer = {word: len(word) for word in string.split()}
print(q6_answer)


"""
    7. Use a nested list comprehension to find all of the numbers from 1–1000 
    that are divisible by any single digit besides 1 (2–9)
"""
q7_answer = [num for num in nums if True in [True for div in range(2, 10) if num % div == 0]]
print("q7_answer: ", q7_answer)

"""
    8. For all the numbers 1–1000, use a nested list/dictionary comprehension to find the highest 
    single digit any of the numbers is divisible by
"""
q8_answer = {num: max([div for div in range(1, 10) if num % div == 0]) for num in nums}
print("q8_answer: ", q8_answer)
