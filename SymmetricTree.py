# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Queue

        # Edge:
        if not root:
            return True

        queue = [(root.left, root.right)]
        while queue:
            left, right = queue.pop(0)

            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            queue.append((left.left, right.right))
            queue.append((left.right,right.left))
        return True   
#---------------------------------------------------------------------
        # Recursion
    def isSymmetric2(self, root):
        # Edge:
        if not root:
            return True

        # Process:
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False    
            return dfs(left.left , right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)