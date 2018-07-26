# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None
        node = head
        copyDict = {}
        
        while node:
            copyDict[node] = RandomListNode(node.label)
            node = node.next
        
        node = head
        
        while node:
            copyDict[node].next = copyDict.get(node.next)
            copyDict[node].random = copyDict.get(node.random)
            node = node.next
        
        return copyDict[head]