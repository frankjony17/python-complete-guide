"""
    Given an array nums, write a function to move all zeroes to the end of it while maintaining
     the relative order of the non-zero elements.
"""

array_1 = [0, 1, 0, 3, 12]
array_2 = [1, 7, 0, 0, 8, 0, 10, 12, 0, 4]


def move_zeroes(nums):
    for _ in list(filter(lambda x: x == 0, nums)):
        nums.remove(0)
        nums.append(0)

    return nums


print(move_zeroes(array_1))
print(move_zeroes(array_2))
