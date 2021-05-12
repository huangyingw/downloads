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
    public TreeNode deleteNode(TreeNode root, int value) 
    {
        TreeNode dummy = new TreeNode (-1), pre = dummy, cur = root;
        dummy.right = root;
        
        while (cur != null) 
        {
            if (cur.val == value) 
            {
                if(pre.left == cur) 
                {
                    pre.left = makeNew(cur);
                }
                else
                {
                    pre.right = makeNew(cur);    
                }
                
                break;
            }
            else if (cur.val < value) 
            {
                pre = cur;
                cur = cur.right;
            }
            else 
            {
                pre = cur;
                cur = cur.left;
            }
        }
        
        return dummy.right;  
    }
    
    private TreeNode makeNew(TreeNode node) 
    {
        if (node.left == null || node.right == null) 
        {
            return node.left == null ? node.right : node.left;
        }
        
        TreeNode left = node.left.right;
        TreeNode right = node.right.left == null ? node.right : node.right.left;
        
        while (right.left != null) 
        {
            right = right.left;
        }
        
        
        right.left = left;
        node.left.right = node.right;
        return node.left;
    }
}
