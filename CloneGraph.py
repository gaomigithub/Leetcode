# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object): 
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if node == None:
            return None

        copyNode = UndirectedGraphNode(node.label)
        dic = {}
        dic[node] = copyNode
        queue = [node]

        while queue:
            cur = queue.pop(0)

            for n in cur.neighbors:
                if n in dic:
                    dic[cur].neighbors.append(dic[n])
                else:
                    nCopy = UndirectedGraphNode(n.label)
                    dic[n] = nCopy
                    dic[cur].neighbors.append(nCopy)
                    queue.append(n)

        return dic[node]


# 类型：BFS
# Time Complexity O(n)
# Space Complexity O(n)

# 思路：

# 找到所有的Nodes，并且储存到字典
# 找到每个Node的Neighbor，并储存到字典
# 有了思路以后，写个Helper用来BFS遍历寻找所有的Node，具体参考getNodes()
# 然后要做的就是把所有的Nodes存储以及他们的Neighbor，参考以下

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    def cloneGraph(self, node):
        if not node: return node
        root = node
        
        # Store Nodes      
        nodes = self.getNodes(node)
        dic = {}
        for node in nodes:
            dic[node] = UndirectedGraphNode(node.label)
            
        # Store Node's Neighbors
        for node in nodes:
            clone_node = dic[node]
            for neighbor in node.neighbors:
                clone_neighbor = dic[neighbor]
                clone_node.neighbors.append(clone_neighbor)
        return dic[root]
            

        
    def getNodes(self, node):
        q = collections.deque([node])
        res = set([node])
        while q:
            head = q.popleft()
            for neighbor in head.neighbors:
                if neighbor not in res:
                    res.add(neighbor)
                    q.append(neighbor)
        return res
