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
    public int longestConsecutive(TreeNode root) 
    {
        if (root == null)
        {
            return 0;
        }
        
        return longestConsecutive(root, 0, root.val - 1);
    }
    
    public int longestConsecutive(TreeNode root, int len, int preVal)
    {
        if (root == null)
        {
            return 0;
        }
        
        if (preVal + 1 == root.val)
        {
            len++;
        }
        else
        {
            len = 0;
        }
        
        int result = Math.max(longestConsecutive(root.left, len, root.val),
                                longestConsecutive(root.right, len, root.val));
        
        System.out.println("root.val --> " + root.val);
        System.out.println("len --> " + len);
        return Math.max(result, len);
    }
}
