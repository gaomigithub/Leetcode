import Queue
import collections

class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    
    def getCloset(s, l):
#babab
#sam
#1
#-1
        if(not s or l == None or len(l) == 0):
          return []

        map = {}
#         a, [1,3]
#         b, [0,2,4]
        for i, c in enumerate(s):
          if(map.get(c)):
            map[c].append(i)
          else:
            map[c] = [i]
#
#ab
# 1
# #babab
# b, [0, 2, 4]
        res = []
        for n in l:

          char = s[n]

          li = map.get(char)

          index = li.index(n)

          if len(li) == 1:
            res.append(-1)
          elif index == 0:
            res.append(li[index + 1])
          else :
            res.append(li[index- 1])

        return res


      
  
    s = "sam"
    
    l = [1]
    
    
    print(getCloset(s, l))     
    

        
        
        
        