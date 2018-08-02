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

// 后续 Follow Up
// Q:如何找湖的数量呢？湖的定义是某个0，其上下左右都是同一个岛屿的陆地。
// A:我们可以先用Number of island的方法，把每个岛标记成不同的ID，然后过一遍整个地图的每个点，如果是0的话，就DFS看这块连通水域是否被同一块岛屿包围，如果出现了不同数字的陆地，则不是湖。

public class NumberOfLakes {
    
    public static void main(String[] args){
        NumberOfLakes nof = new NumberOfLakes();
        int[][] world = {{1,1,1,0,1},{1,0,0,1,0},{1,1,1,1,1,},{0,1,1,0,1},{0,1,1,1,1}};
        System.out.println(nof.numberOfLakes(world));
    }
    
    public int numberOfLakes(int[][] world){
        int islandId = 2;
        for(int i = 0; i < world.length; i++){
            for(int j = 0; j < world[0].length; j++){
                if(world[i][j] == 1){
                    findIsland(world, i, j, islandId);
                    islandId++;
                }
            }
        }
        int lake = 0;
        for(int i = 0; i < world.length; i++){
            for(int j = 0; j < world[0].length; j++){
                if(world[i][j] == 0){
                    // 找到当前水域的邻接陆地编号
                    int currId = 0;
                    if(i > 0) currId = (world[i - 1][j] != 0 ? world[i - 1][j] : currId);
                    if(j > 0) currId = (world[i][j - 1] != 0 ? world[i][j - 1] : currId);
                    if(i < world.length - 1) currId = (world[i + 1][j] != 0 ? world[i + 1][j] : currId);
                    if(j < world[0].length - 1) currId = (world[i][j + 1] != 0 ? world[i][j + 1] : currId);
                    // 如果该点是湖，加1
                    if(findLake(world, i, j, currId)){
                        lake++;
                    }
                }
            }
        }
        return lake;
    }
    
    private boolean findLake(int[][] world, int i, int j, int id){
        // 将当前水域标记成周边岛屿的数字
        world[i][j] = id;
        // 找上下左右是否是同一块岛屿的陆地，如果是水域则继续DFS，如果当前水域是边界也说明不是湖
        boolean up = i != 0 
                && (world[i - 1][j] == id 
                || (world[i - 1][j] == 0 && findLake(world, i - 1, j, id)));
        boolean down = i != world.length - 1 
                && (world[i + 1][j] == id 
                || (world[i + 1][j] == 0 && findLake(world, i + 1, j, id)));
        boolean left = j != 0 
                && (world[i][j - 1] == id 
                || (world[i][j - 1] == 0 && findLake(world, i, j - 1, id)));
        boolean right = j != world[0].length - 1 
                && (world[i][j + 1] == id 
                || (world[i][j + 1] == 0 && findLake(world, i, j + 1, id)));
        return up && down && right && left;
    }
    
    private void findIsland(int[][] world, int i, int j, int id){
        world[i][j] = id;
        if(i > 0 && world[i - 1][j] == 1) findIsland(world, i - 1, j, id);
        if(j > 0 && world[i][j - 1] == 1) findIsland(world, i, j - 1, id);
        if(i < world.length - 1 && world[i + 1][j] == 1) findIsland(world, i + 1, j, id);
        if(j < world[0].length - 1 && world[i][j + 1] == 1) findIsland(world, i, j + 1, id);
    }
}