# Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

# The number at the ith position is divisible by i.
# i is divisible by the number at the ith position.
# Now given N, how many beautiful arrangements can you construct?

# Example 1:
# Input: 2
# Output: 2
# Explanation: 

# The first beautiful arrangement is [1, 2]:

# Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

# Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

# The second beautiful arrangement is [2, 1]:

# Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

# Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
# Note:
# N is a positive integer and will not exceed 15.


# 解题思路：
# http://bookshadow.com/weblog/2017/02/19/leetcode-beautiful-arrangement/
# 记忆化搜索（Memoization）
# 搜索函数定义为：solve(idx, nums)
# 其中idx为当前数字的下标，nums为剩余待选数字
# 初始令idx = 1, nums = [1 .. N]
# 遍历nums，记当前数字为n，除n以外的其余元素为nums'
# 若n满足题设的整除条件，则将solve(idx + 1, nums')累加至答案

class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        cache = dict()
        def solve(idx, nums):
            if not nums: return 1
            key = idx, tuple(nums)
            if key in cache: return cache[key]
            ans = 0
            for i, n in enumerate(nums):
                if n % idx == 0 or idx % n == 0:
                    ans += solve(idx + 1, nums[:i] + nums[i+1:])
            cache[key] = ans
            return ans
        return solve(1, range(1, N + 1))
