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
    public TreeNode upsideDownBinaryTree(TreeNode root)
    {
        if (root == null)
        {
            return null;
        }

        return upsideDownBinaryTreeHelper(root, null);
    }

    private TreeNode upsideDownBinaryTreeHelper(TreeNode root, TreeNode parent)
    {
        if (root == null)
        {
            return parent;
        }

        TreeNode newNode = upsideDownBinaryTreeHelper(root.left, root);
        root.left = parent == null ? null : parent.right;
        root.right = parent;
        return newNode;
    }
}
