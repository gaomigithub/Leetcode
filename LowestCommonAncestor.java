public class LowestCommonAncestor {
    public TreeNode getAncestor(TreeNode root, TreeNode node1, TreeNode node2) {
        if (root == null || root == node1 || root == node2) {
            return root;
        }

        // Divide
        TreeNode left = getAncestor(root.left, node1, node2);
        TreeNode right = getAncestor(root.right, node1, node2);

        // Conquer
        // 如果找到了就返回这个LCA
        if (left != null && right != null) {
            return root;
        }

        if (left != null) {
            return left;
        }

        if (right != null) {
            return right;
        }

        // 如果都没，就返回null
        return null;
    }
}
