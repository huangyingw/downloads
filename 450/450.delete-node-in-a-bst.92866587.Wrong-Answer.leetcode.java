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
    public TreeNode deleteNode(TreeNode root, int key) 
    {
        if (root == null)
        {
            return root;    
        }
        
        if (root.val == key)
        {
            if (root.left != null)
            {
                root.val = root.left.val;
                root.left = null;
            }
            else if (root.right != null)
            {
                root.val = root.right.val;
                root.right = null;
            }
            else
            {
                return null;
            }
        }
        else if (root.val < key)
        {
            root.right = deleteNode(root.right, key);   
        }
        else
        {
            root.left = deleteNode(root.left, key);   
        }
        
        return root;
    }
}
