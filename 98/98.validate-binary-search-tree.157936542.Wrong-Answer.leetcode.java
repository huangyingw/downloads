public class Solution
{
    public Boolean isValidBST(TreeNode root, int lower, int upper)
    {
        if (root == null)
        {
            return true;
        }

        return root.val > lower && root.val < upper
               && isValidBST(root.left, lower, root.val)
               && isValidBST(root.right, root.val, upper);
    }

    public boolean isValidBST(TreeNode root)
    {
        return isValidBST(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }
}


