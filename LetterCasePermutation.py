# Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

# Examples:
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

# Input: S = "3z4"
# Output: ["3z4", "3Z4"]

# Input: S = "12345"
# Output: ["12345"]
# Note:

# S will be a string with length at most 12.
# S will consist only of letters or digits.

"""
ASCII:
Upper case A-Z: 65 - 90
Lower case a-z: 97 - 122
'a' - 'Z' = 32
"""

# Solution: DFS
# Time complexity: O(n*2^l), l = # of letters in the string
# Space complexity: O(n) + O(n*2^l)

"""
Author: Huahua
Running time: 92 ms
"""
class Solution:
    def letterCasePermutation(self, S):
        ans = []
 
        def dfs(S, i, n):
            if i == n:
                ans.append(''.join(S))
                return
        
            dfs(S, i + 1, n)      
            if not S[i].isalpha(): return      
            S[i] = chr(ord(S[i]) ^ (1<<5))
            dfs(S, i + 1, n)
            S[i] = chr(ord(S[i]) ^ (1<<5))
    
        dfs(list(S), 0, len(S))
        return ans