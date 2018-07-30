// There are a total of n courses you have to take, labeled from 0 to n - 1.

// Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

// Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

// For example:

// 2, [[1,0]]

// There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

// 2, [[1,0],[0,1]]

// There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

// Note:
// The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented


// BFS Solution
/**
 * 定义二维数组graph来表示这个有向图，一位数组in来表示每个顶点的入度。
 * 我们开始先根据输入来建立这个有向图，并将入度数组也初始化好。
 * 然后我们定义一个queue变量，将所有入度为0的点放入队列中，然后开始遍历队列，
 * 从graph里遍历其连接的点，每到达一个新节点，将其入度减一，
 * 如果此时该点入度为0，则放入队列末尾。直到遍历完队列中所有的值，
 * 若此时还有节点的入度不为0，则说明环存在，返回false，反之则返回true。
 */
public class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        if(prerequisites == null){
            throw new IllegalArgumentException("illegal prerequisites array");
        }
     
        int len = prerequisites.length;
     
        if(numCourses == 0 || len == 0){
            return true;
        }
     
        // counter for number of prerequisites
        int[] pCounter = new int[numCourses];
        for(int i=0; i<len; i++){
            pCounter[prerequisites[i][0]]++;
        }
     
        //store courses that have no prerequisites
        LinkedList<Integer> queue = new LinkedList<Integer>();
        for(int i=0; i<numCourses; i++){
            if(pCounter[i]==0){
                queue.add(i);
            }
        }
     
        // number of courses that have no prerequisites
        int numNoPre = queue.size();
     
        while(!queue.isEmpty()){
            int top = queue.remove();
            for(int i=0; i<len; i++){
                // if a course's prerequisite can be satisfied by a course in queue
                if(prerequisites[i][1]==top){
                    pCounter[prerequisites[i][0]]--;
                    if(pCounter[prerequisites[i][0]]==0){
                        numNoPre++;
                        queue.add(prerequisites[i][0]);
                    }
                }
            }
        }
     
        return numNoPre == numCourses;
    }
}

// ------------------------------------------------------------------------------
// DFS Solution

public class Solution2 {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        if(prerequisites == null){
            throw new IllegalArgumentException("illegal prerequisites array");
        }
     
        int len = prerequisites.length;
     
        if(numCourses == 0 || len == 0){
            return true;
        }
     
        //track visited courses
        int[] visit = new int[numCourses];
     
        // use the map to store what courses depend on a course 
        HashMap<Integer,ArrayList<Integer>> map = new HashMap<Integer,ArrayList<Integer>>();
        for(int[] a: prerequisites){
            if(map.containsKey(a[1])){
                map.get(a[1]).add(a[0]);
            }else{
                ArrayList<Integer> l = new ArrayList<Integer>();
                l.add(a[0]);
                map.put(a[1], l);
            }
        }
     
        for(int i=0; i<numCourses; i++){
            if(!canFinishDFS(map, visit, i))
                return false;
        }
     
        return true;
    }
     
    private boolean canFinishDFS(HashMap<Integer,ArrayList<Integer>> map, int[] visit, int i){
        if(visit[i]==-1) 
            return false;
        if(visit[i]==1) 
            return true;
     
        visit[i]=-1;
        if(map.containsKey(i)){
            for(int j: map.get(i)){
                if(!canFinishDFS(map, visit, j)) 
                    return false;
            }
        }
     
        visit[i]=1;
     
        return true;
    }
}
