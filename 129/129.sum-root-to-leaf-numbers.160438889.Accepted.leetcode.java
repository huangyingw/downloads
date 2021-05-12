public class Solution
{

    private int dfs(TreeNode root, int base)
    {
        if (root.left == null && root.right == null)
        {
            return base;
        }

        int sum = 0;

        if (root.left != null)
        {
            sum += dfs(root.left, base * 10 + root.left.val);
        }

        if (root.right != null)
        {
            sum += dfs(root.right, base * 10 + root.right.val);
        }

        return sum;
    }

    public int sumNumbers(TreeNode root)
    {
        if (root == null)
        {
            return 0;
        }

        return dfs(root, root.val);
    }
}

