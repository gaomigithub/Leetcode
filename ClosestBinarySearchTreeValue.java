// Given a non-empty binary search tree and a target value, 
// find the value in the BST that is closest to the target.


// Java Solution 1 - Recursion

// Recursively traverse down the root. When target is less than root, go left; 
// when target is greater than root, go right.
public class Solution {
    int goal;
    double min = Double.MAX_VALUE;
 
    public int closestValue(TreeNode root, double target) {
        helper(root, target);
        return goal;
    }
 
    public void helper(TreeNode root, double target){
        if(root==null)
            return;
 
        if(Math.abs(root.val - target) < min){
            min = Math.abs(root.val-target);
            goal = root.val;
        } 
 
        if(target < root.val){
            helper(root.left, target);
        }else{
            helper(root.right, target);
        }
    }
}

// Java Solution 2 - Iteration
class solution2 {
    public int closestValue(TreeNode root, double target) {
        double min=Double.MAX_VALUE;
        int result = root.val;
     
        while(root!=null){
            if(target>root.val){
     
                double diff = Math.abs(root.val-target);
                if(diff<min){
                    min = Math.min(min, diff);
                    result = root.val;
                }
                root = root.right;
            }else if(target<root.val){
     
                double diff = Math.abs(root.val-target);
                if(diff<min){
                    min = Math.min(min, diff);
                    result = root.val;
                }
                root = root.left;
            }else{
                return root.val;
            }
        }
     
        return result;
    }
}