# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]


# Complex: O(logn)
class FindFirstandLastPositionofElementinSortedArray:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        if length == 0:
            return [-1,-1]
        if nums[0] <= target and nums[-1] >= target:
            left,right = 0,length-1

            while left <= right:
                mid = (left+right) // 2

                if nums[mid] == target:
                    right = left = mid

                    while left-1 >= 0 and nums[left-1] == target:
                        left -= 1
                    while right+1 <= length-1 and nums[right+1] == target:
                        right += 1
                    return [left,right]

                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

        return [-1,-1]