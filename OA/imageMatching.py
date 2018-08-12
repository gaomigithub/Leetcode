import Queue
import collections

class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    global count
    count = 0
    global neibors
    neibors = [[0,1],[0,-1],[1,0],[-1,0]]
    
    def isMatch(self, grid1, grid2):
        if not grid1 or not grid2:
            return 0

        h, l= len(grid1), len(grid1[0])
        visited = [[False]*l]*h

        for i in range(h):
            for j in range(l):
                if(grid2[i][j] == 1 and grid1[i][j] == 1 and visited[i][j] == False):
                   visited[i][j] = True   
                   q = collections.deque((i,j))
                   self.bfs(q, grid1, grid2, visited)
                                
                  
        return count
                        
    def bfs(self, q, grid1, grid2, visited):
        while(q):
          cur = q.popleft()
          print("cur")
          print(q)
          for neibor in neibors:
            print(neibor)
            i = cur[0] + neibor[0]
            j = cur[1] + neibor[1]
            
            if (outBound(i, j, grid1) or visited[i][j]):
              continue
            
            
            if (grid2[i][j] == 1 and grid1[i][j] == 1):
              visited[i][j] = True
              q.push([newx, newy])
            #not match  
            else:
              return
        
        count += 1
        return 

      

if __name__ == '__main__':

  
    g1 = [
         [0, 1, 0, 1],
         [1, 0, 0, 1],
         [0, 0, 1, 1],
         [0, 0, 1, 1]]
    
    g2 = [[0, 1, 0, 1],
          [1, 0, 0, 0], 
          [0, 0, 1, 1],
          [0, 0, 1, 1]] 
  
    
    
    g6 = [[0, 1, 0, 0],
          [1, 0, 0, 0], 
          [0, 0, 0, 0], 
          [0, 0, 0, 0]]
    
    output = 2
    s = Solution()
    visited = [[False]*4]*3
    print s.isMatch(g1, g2)
#     for g in [g0, g1, g2, g3, g4, g5]:
#         print s.numIslands(g)


        
        
        
        
        
        