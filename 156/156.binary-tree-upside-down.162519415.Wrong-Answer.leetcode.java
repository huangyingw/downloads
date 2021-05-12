public class Solution
{
    private TreeNode out = null;

    public TreeNode upsideDownBinaryTree(TreeNode root)
    {
        TreeNode dummy = new TreeNode(0);
        dummy.left = new TreeNode(0);
        out = dummy;
        postorder(root);
        return dummy.right;
    }

    private void postorder(TreeNode root)
    {
        if (root == null)
        {
            return;
        }

        postorder(root.left);
        postorder(root.right);

        if (out.left == null)
        {
            out.left = root;
            out.left.left = null;
            out.left.right = null;
        }
        else if (out.right == null)
        {
            out.right = root;
            out.right.left = null;
            out.right.right = null;
        }

        if (out.left != null && out.right != null)
        {
            out = out.right;
        }
    }
}


