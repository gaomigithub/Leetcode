# https://leetcode.com/problems/sliding-window-maximum/

# Given an array nums, there is a sliding window of size k 
# which is moving from the very left of the array to the very right. 
# You can only see the k numbers in the window. 
# Each time the sliding window moves right by one position.

# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Therefore, return the max sliding window as [3,3,5,5,6,7].

# Note: 
# You may assume k is always valid, ie: 1 ≤ k ≤ input array’s size for non-empty array.

# Follow up:
# Could you solve it in linear time?


# 遍历数组nums，使用双端队列deque维护滑动窗口内有可能成为最大值元素的数组下标

# 由于数组中的每一个元素至多只会入队、出队一次，因此均摊时间复杂度为O(n)

# 记当前下标为i，则滑动窗口的有效下标范围为[i - (k - 1), i]

# 若deque中的元素下标＜ i - (k - 1)，则将其从队头弹出，deque中的元素按照下标递增顺序从队尾入队。

# 这样就确保deque中的数组下标范围为[i - (k - 1), i]，满足滑动窗口的要求。

# 当下标i从队尾入队时，顺次弹出队列尾部不大于nums[i]的数组下标（这些被弹出的元素由于新元素的加入而变得没有意义）

# deque的队头元素即为当前滑动窗口的最大值

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
        dq = collections.deque()
        ans = []
        for i in range(len(nums)):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            if dq[0] == i - k:
                dq.popleft()
            if i >= k - 1:
                ans.append(nums[dq[0]])
        return ans


# class Solution:
#   def maxSlidingWindow(self, nums, k):
#     if not nums: return []    
#     return [max(nums[i:i+k]) for i in range(len(nums) - k + 1)]