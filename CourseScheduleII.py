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

        for v, w in prerequisites:
            graph[w].append(v)
            indegree[v] += 1

        # find zero indegree
        zero = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                zero.append(i)

        res = []
        while zero:
            cur = zero.pop(0)
            res.append(cur)

            for n in graph[cur]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    zero.append(n)

        return res if sum(indegree) == 0 else []

# 就把每次pop出来的数存到一个数组返回即可。
# 类型：BFS
# Time Complexity O(n)
# Space Complexity O(n)

class Solution(object):
    def findOrder(self, n , edges):
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
        res = []
        while q:
            node = q.popleft()
            visited += 1
            res.append(node)
            for neigh in graph[node]:
                in_degrees[neigh] -= 1
                if in_degrees[neigh] == 0:
                    q.append(neigh)
        return res if visited == n else []