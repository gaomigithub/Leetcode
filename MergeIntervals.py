# Problem:

# Given a collection of intervals, merge all overlapping intervals.

# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].

class Solution(object):
    def merge(self, intervals):
        ans = []
        for interval in sorted(intervals, key=lambda x: x.start):
            if not ans or interval.start > ans[-1].end: #集合开头去和最后一个元素的尾巴比
                ans.append(interval)
            else:
                ans[-1].end = max(ans[-1].end, interval.end) #当前集合最后一个的结尾取最大的那个
        return ans