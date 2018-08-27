# There are a total of n courses you have to take, labeled from 0 to n-1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

# Example 1:

# Input: 2, [[1,0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.
# Note:

# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.


# Hint: cannot have a circle

# BFS(topo sort)
# O(n) time, O(n) space
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        # find zero indegree
        zero = []
        for i in range(numCourses):
            if indegree[i] == 0:
                zero.append(i)

        while zero:
            cur = zero.pop(0)

            if cur in graph:
                temp = graph[cur]
                del graph[cur]

                for n in temp:
                    indegree[n] -= 1
                    if indegree[n] == 0:
                        zero.append(n)

        return len(graph) == 0 and sum(indegree) == 0


# 类型：BFS
# Time Complexity O(n)
# Space Complexity O(n)

# Topological Sorting题
# 首先构建一个图，因为题目没有提供。
# 然后创建一个入度数组。
# 把入度数组里面为0的课丢进Queue，表示这门课无需Pre-req，然后对这门课的所有邻居的入度减1。更新完邻居的入度后，如果发现邻居里面有入度为0，则将其丢进Queue继续迭代。
class Solution(object):
    def canFinish(self, n, edges):
        from collections import deque
        in_degrees = [0 for i in range(n)]   #入度记录一门课需要上几个pre_req
        graph = {i: set() for i in range(n)}   #画一幅图

        # 构建图以及入度
        for i, j in edges:
            in_degrees[i] += 1  
            graph[j].add(i) 

        # 如果课没有pre_req，扔到Queue里
        q = deque()
        for i, pre_req in enumerate(in_degrees):    
            if not pre_req:
                q.append(i)

        # 进行BFS操作
        visited = 0
        while q:
            node = q.popleft()
            visited += 1
            for neigh in graph[node]:
                in_degrees[neigh] -= 1
                if in_degrees[neigh] == 0:
                    q.append(neigh)
        return visited == n
        