public class Solution
{
    private int max;
    public int findMax(TreeNode root)
    {
        if (root == null)
        {
            return 0;
        }

        int left = Math.max(findMax(root.left), 0);
        int right = Math.max(findMax(root.right), 0);
        max = Math.max(max, root.val + left + right);
        return root.val + Math.max(left, right);
    }
    public int maxPathSum(TreeNode root)
    {
        max = Integer.MIN_VALUE;
        findMax(root);
        return max;
    }
}

