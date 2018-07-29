# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete at most two transactions.

# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

# Example 1:

# Input: [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
#              Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
# Example 2:

# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#              engaging multiple transactions at the same time. You must sell before buying again.
# Example 3:

# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

# 因为最多只能进行两次交易，所以可以将时间一划为二，分别找这两段时间内进行一次
# （也可能不进行交易）所能获得的最大利润（方法参见 Best Time to Buy and Sell Stock），
# 将两者相加就是在这种划分情况下最多进行两次交易所能获取的最大利润。
# 遍历所有的划分可能，就能找出最终的最大利润。
# 如果每次都将时间段直接调用Best Time to Buy and Sell Stock的方法，复杂的用例会超时。
# 我们可以先从前往后遍历，并缓存最多进行一次交易所能获取的最大利润；
# 再从后往前遍历计算最多进行一次交易所能获取的最大利润，
# 与对应的缓存相加就是在一次划分下的最大利润。

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1:
            return 0
        p1 = [0] * n
        p2 = [0] * n
        
        minV = prices[0]
        for i in range(1,n):
            minV = min(minV, prices[i])
            p1[i] = max(prices[i] - minV, p1[i - 1])
        
        maxV = prices[-1]
        for i in range(n-2, -1, -1):
            maxV = max(maxV, prices[i])
            p2[i] = max(p2[i + 1], maxV - prices[i])
        
        res = 0
        for i in range(n):
            res = max(res, p1[i] + p2[i])
        return res