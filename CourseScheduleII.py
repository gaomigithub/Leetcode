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