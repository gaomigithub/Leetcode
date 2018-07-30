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
