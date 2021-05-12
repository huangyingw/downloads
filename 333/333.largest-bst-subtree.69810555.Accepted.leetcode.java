/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int largestBSTSubtree(TreeNode root){  
        if(isBST(root)){  
            return size(root);  
        }  
        return Math.max(largestBSTSubtree(root.left), largestBSTSubtree(root.right));  
    }  
  
    private int size(TreeNode root) {  
        if(root == null)  
            return 0;  
        return 1 + size(root.left) + size(root.right);  
    }  
  
    private boolean isBST(TreeNode root) {  
          
        return isBST(root, Integer.MIN_VALUE, Integer.MAX_VALUE);  
    }  
      
    private boolean isBST(TreeNode root, int min, int max) {  
        if(root == null)  
            return true;  
        if(root.val >= max)  
            return false;  
        else if(root.val <= min)  
            return false;  
          
        return isBST(root.left, min, root.val) && isBST(root.right, root.val, max);  
    } 
}
