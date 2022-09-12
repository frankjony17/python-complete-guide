"""
    An array is monotonic if it is either monotone increasing or monotone decreasing.

    An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
    An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

    Given an integer array nums, return true if the given array is monotonic, or false otherwise.
"""

array_1 = [6, 5, 4, 4]
array_2 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
array_3 = [1, 1, 2, 3, 7]


def monotonic(nums):
    return (all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) or
            all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1)))


print(monotonic(array_1))
print(monotonic(array_2))
print(monotonic(array_3))
