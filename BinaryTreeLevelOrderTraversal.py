# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# 将树每一层的节点存在一个列表中，遍历列表中的元素，如果该节点有左右节点的话，
# 就把它们加入一个临时列表，这样当遍历结束时，下一层的节点也按照顺序存储好了，
# 不断循环直到下一层的列表为空。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        curr_level = [root]
        while curr_level:
            level_result = []
            next_level = []
            for temp in curr_level:
                level_result.append(temp.val)
                if temp.left:
                    next_level.append(temp.left)
                if temp.right:
                    next_level.append(temp.right)
            result.append(level_result)
            curr_level = next_level
        return result


# 类型：BFS
# Time Complexity O(n)
# Space Complexity O(n)


# BFS的题解思路。

# 这里new_q也可以命名成next_level，同样q可以命名为cur_level，但因为太长，我选择放弃。

# 通过一个temp的数组new_q来存储下一层的node，
# 每次迭代完成后，把temp数组的node更新到q里面用于下一次迭代，并存储至res

class Solution(object):
    def levelOrder(self, root):
        res = []
        if not root: 
            return res
        q = [root]
        while q :
            res.append([node.val for node in q])
            new_q = []
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q
        return res