
'''
Given a collection of distinct numbers, return all possible permutations.
For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        def dfs(nums, temp):
            if len(temp) == len(nums): # 当temp的长度和一开始传进去的长度一样的时候
                self.res.append(temp[:]) # 不能直接传temp
            
            for i in range(len(nums)):
                if nums[i] in temp: # 如果这个数已经在里面了，比如不可能11或者22
                    continue
                
                temp.append(nums[i])
                dfs(nums, temp)
                temp.pop()
        dfs(nums, [])
        return self.res


class Solution2(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.get_permute([], nums, result)
        return result

    def get_permute(self, current, num, result):
        if not num:
            result.append(current + [])
            return
        for i, v in enumerate(num):
            current.append(num[i])
            self.get_permute(current, num[:i] + num[i + 1:], result)
            current.pop()


if __name__ == "__main__":
    assert Solution().permute([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]