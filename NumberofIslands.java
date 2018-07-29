// Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

// Example 1:

// Input:
// 11110
// 11010
// 11000
// 00000

// Output: 1
// Example 2:

// Input:
// 11000
// 11000
// 00100
// 00011

// Output: 3


// 两种进行图遍历的基本方法：DFS和BFS。

// 我们需要依次从每个点出发，利用BFS和DFS，找到所有与其在同一个联通分量的点。如果某个点已经在之前的某个联通分量中被遍历过了，我们不需要重复遍历它。

// 重复以上两个步骤，直到图中的所有点都被遍历过。那么最后一个问题就是，我如何记录已经访问过某个点？

// 比较直观的想法，就是我创建一个和原input matrix size一样的boolean矩阵，访问过的位置即为true。
// 这个方法非常直观，但是需要额外的空间。更好的方法是，当我们扫过1了之后，我们就用另一个数字代替它，
// 但这种方法会修改input matrix，是否可以采用，在实际面试中，需要和面试官进行讨论。


class NumberofIslands {
    public int numberOfIslandsI (int[][] matrix) {
        // sanity check
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }
        int count = 0;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == 1) {
                    count++;
                    dfs(matrix, i , j);
                }
            }
        }
        return count;
    }
    
    static final int[][] dirs = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
    private void dfs(int[][] matrix, int x, int y) {
        // base case
        if (x < 0 || x >= matrix.length || y < 0 || y >= matrix[0].length) {
            return;
        }
        if (matrix[x][y] == 0) {
            return;
        }
    
        // recursive part
        matrix[x][y] = 2;  // matrix[x][y] = 0; 证明已经经过
        for (int[] dir : dirs) {
            int neiX = x + dir[0];
            int neiY = y + dir[1];
            dfs(matrix, neiX, neiY);
        }
    }
}