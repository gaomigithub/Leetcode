# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1

# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3

# DFS
# 我们遍历矩阵的每一个点，对每个点都尝试进行一次深度优先搜索，如果搜索到1，就继续向它的四周搜索。
# 同时我们每找到一个1，就将其标为0，
# 这样就能把整个岛屿变成0。我们只要记录对矩阵遍历时能进入多少次搜索，就代表有多少个岛屿。
class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    self.dfs(grid, row, col, i, j)
                    count += 1
        return count

    def dfs(self, grid, row, col, x, y):
        if grid[x][y] == '0':
            return
        grid[x][y] = '0'

        if x != 0:
            self.dfs(grid, row, col, x - 1, y)
        if x != row - 1:
            self.dfs(grid, row, col, x + 1, y)
        if y != 0:
            self.dfs(grid, row, col, x, y - 1)
        if y != col - 1:
            self.dfs(grid, row, col, x, y + 1)


# BFS
class Solution2:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        ans = 0
        if not len(grid):
            return ans
        m, n = len(grid), len(grid[0])
        visited = [ [False] * n for x in range(m) ] # m * n
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1' and not visited[x][y]:
                    ans += 1
                    self.bfs(grid, visited, x, y, m, n)
        return ans

    def bfs(self, grid, visited, x, y, m, n):
        dz = zip( [1, 0, -1, 0], [0, 1, 0, -1] )
        queue = [ (x, y) ]
        visited[x][y] = True
        while queue:
            front = queue.pop(0)
            for p in dz:
                np = (front[0] + p[0], front[1] + p[1])
                if self.isValid(np, m, n) and grid[np[0]][np[1]] == '1' and not visited[np[0]][np[1]]:
                    visited[ np[0] ][ np[1] ] = True
                    queue.append(np)

    def isValid(self, np, m, n):
        return np[0] >= 0 and np[0] < m and np[1] >= 0 and np[1] < n