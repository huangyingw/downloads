public class Solution
{
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p)
    {
        if (root == null)
        {
            return null;
        }

        TreeNode successor = null;

        while (root != null)
        {
            if (root.val > p.val)
            {
                successor = root;
                root = root.left;
            }
            else if (root.val < p.val)
            {
                root = root.right;
            }
            else
            {
                break;
            }
        }

        if (root.right == null)
        {
            return successor;
        }

        return root;
    }
}
