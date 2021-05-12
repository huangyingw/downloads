/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution 
{
    public int sumOfLeftLeaves(TreeNode root) 
    {
        return sumOfLeftLeaves(root, false);
    }
    
    public int sumOfLeftLeaves(TreeNode root, boolean isLeft)
    {
        if (root == null)
        {
            return 0;
        }
        
        if (root.left == null && root.right == null && isLeft)
        {
            return root.val;
        }
        
        int left = sumOfLeftLeaves(root.left, true);
        int right = sumOfLeftLeaves(root.right, false);
        
        return left + right;
    }
}
