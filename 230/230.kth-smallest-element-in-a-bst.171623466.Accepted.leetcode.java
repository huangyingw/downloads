public class Solution
{
    private int count = 0;
    private int result = -1;

    public int kthSmallest(TreeNode root, int k)
    {
        inorderTraversal(root, k);
        return result;
    }

    private void inorderTraversal(TreeNode root, int k)
    {
        if (root == null)
        {
            return;
        }

        inorderTraversal(root.left, k);

        if (++count == k)
        {
            result = root.val;
        }

        inorderTraversal(root.right, k);
    }
}

