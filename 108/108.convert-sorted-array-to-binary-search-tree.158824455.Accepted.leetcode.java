public class Solution
{
    public TreeNode sortedArrayToBST(int[] num)
    {
        return dfs(num, 0, num.length - 1);
    }
    public TreeNode dfs(int [] num, int l, int r)
    {
        if (l > r)
        {
            return null;
        }

        int m = (l + r) / 2;
        TreeNode root = new TreeNode(num[m]);
        root.left = dfs(num, l, m - 1);
        root.right = dfs(num, m + 1, r);
        return root;
    }
}

