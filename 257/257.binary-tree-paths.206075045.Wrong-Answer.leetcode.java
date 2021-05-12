public class Solution
{
    public List<String> binaryTreePaths(TreeNode root)
    {
        List<String> result = new ArrayList<String>();

        if (root == null)
        {
            return result;
        }

        binaryTreePathsDFS(root, "" + root.val, result);
        return result;
    }

    void binaryTreePathsDFS(TreeNode root, String out, List<String> result)
    {
        if (root == null)
        {
            return;
        }

        if (root.left == null && root.right == null)
        {
            out += root.val;
            result.add(out);
        }

        out += root.val + "->";
        binaryTreePathsDFS(root.left, out, result);
        binaryTreePathsDFS(root.right, out, result);
    }
}

