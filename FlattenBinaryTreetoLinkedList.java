//Given a binary tree, flatten it to a linked list in-place.
//
//        For example, given the following tree:
//
//        1
//        / \
//        2   5
//        / \   \
//        3   4   6
//        The flattened tree should look like:
//
//        1
//        \
//        2
//        \
//        3
//        \
//        4
//        \
//        5
//        \
//        6

import jdk.nashorn.api.tree.Tree;

import java.util.Stack;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class FlattenBinaryTreetoLinkedList {
    private TreeNode lastNode = null;


    public void flatten(TreeNode root) {
        if (root == null) {
            return;
        }

        if (lastNode != null) {
            lastNode.left = null;
            lastNode.right = root;
        }

        lastNode = root;
        TreeNode right = root.right;
        flatten(root.left);
        flatten(right);
    }
}

// 非递归
class non_recosive {
    public void flatten(TreeNode root) {
        if (root == null) {
            return;
        }

        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);

        while (!stack.empty()) {
            TreeNode node = stack.pop();
            if (node.right != null) {
                stack.push(node.right);
            }
            if (node.left != null) {
                stack.push(node.left);
            }

            // connect
            node.left = null;
            if (stack.empty()) {
                node.right = null;
            } else {
                node.right = stack.peek();
            }
        }
    }
}