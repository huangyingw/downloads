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
        
        int left = sumOfLeftLeaves(root.left, true);
        int right = sumOfLeftLeaves(root.right, false);
        
        if (left == 0 && right == 0 && isLeft)
        {
            return root.val;
        }
        else
        {
            return left + right;
        }
    }
}
