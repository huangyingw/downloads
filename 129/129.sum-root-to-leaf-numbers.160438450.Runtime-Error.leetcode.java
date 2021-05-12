public class Solution
{

    private int sumNumbers(TreeNode root, int base)
    {
        if (root.left == null && root.right == null)
        {
            return base;
        }

        return sumNumbers(root.left, base * 10 + root.left.val) + sumNumbers(root.right, base * 10 + root.right.val);
    }

    public int sumNumbers(TreeNode root)
    {
        if (root == null)
        {
            return 0;
        }

        return sumNumbers(root, root.val);
    }
}

