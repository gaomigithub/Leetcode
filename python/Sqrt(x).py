# Implement int sqrt(int x).

# Compute and return the square root of x.

# x is guaranteed to be a non-negative integer.

# Example 1:

# Input: 4
# Output: 2

# Example 2:

# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842...

class Solution:
  def mySqrt(self, a):
    l = 1
    r = a
    while l <= r:
      m = l + (r - l) // 2
      if m * m > a:
        r = m - 1
      else:
        l = m + 1
    return r;