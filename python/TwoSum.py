# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# Python3
class Solution:
    def twoSum(self, num, target):
        dict = {}
        for i in range(len(num)):
            x = num[i]
            if target-x in dict:
                return (dict[target-x], i)
            dict[x] = i
        