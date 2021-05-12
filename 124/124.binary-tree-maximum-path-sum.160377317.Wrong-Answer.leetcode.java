public class Solution
{

    private int max_sum;

    public int dfs(TreeNode root)
    {
        if (root == null)
        {
            return 0;
        }

        int left = maxPathSum(root.left);
        int right = maxPathSum(root.right);
        int sum = root.val;

        if (left > 0)
        {
            sum += left;
        }

        if (right > 0)
        {
            sum += right;
        }

        max_sum = Math.max(max_sum, sum);
        return Math.max(left, right) > 0 ? Math.max(left, right) + root.val : root.val;
    }

    public int maxPathSum(TreeNode root)
    {
        max_sum = Integer.MIN_VALUE;
        dfs(root);
        return max_sum;
    }
}

