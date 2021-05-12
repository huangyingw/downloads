public class Solution
{
    public TreeNode upsideDownBinaryTree(TreeNode root)
    {
        return dfs(root, null);
    }

    TreeNode dfs(TreeNode root, TreeNode parent)
    {
        if (root == null)
        {
            return parent;
        }

        TreeNode newRoot = dfs(root.left, root);
        root.left = parent == null ? null : parent.right;
        root.right = parent;
        return newRoot;
    }
}

