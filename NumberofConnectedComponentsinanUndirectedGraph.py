# Example 1:

#   0           3
#   |           |
#   1 --- 2     4

# Given n = 5 and edges = [[0,1], [1,2], [3,4]], return 2.

# Example 2:

#   0           4
#   |           |
#   1 --- 2 --- 3

# Given n = 5 and edges = [[0,1], [1,2], [2,3], [3,4]], return 1.


# BFS Solution:
import collections

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        neighbors = collections.defaultdict(set)
        # connect neighbors
        for v, w in edges:
            neighbors[v].add(w)
            neighbors[w].add(v)

        visited = [False] * n
        res = 0

        # for each node
        for i in range(n):
            if visited[i] == False: # if it not visited
                res += 1
                queue = [i]
                visited[i] = True

                while queue:
                    cur = queue.pop(0)

                    for k in neighbors[cur]:
                        if visited[k] == False:
                            queue.append(k)
                            visited[k] = True
        return res