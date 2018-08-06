# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

# Solution: DFS
# Time complexity: O(2^n)
# Space complexity: O(k + n)

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.generate(n, n, "", result)
        return result

    def generate(self, left, right, str, result):
        if left == 0 and right == 0:
            result.append(str)
            return
        # 开始一层一层盖盖子，盖好一层就-1
        if left > 0:
            self.generate(left - 1, right, str + "(", result)
        if right > left:
            self.generate(left, right - 1, str + ")", result)