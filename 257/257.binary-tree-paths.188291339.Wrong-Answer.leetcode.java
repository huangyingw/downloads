public class Solution
{
    public List<String> binaryTreePaths(TreeNode root)
    {
        List<String> result = new ArrayList<String>();
        binaryTreePathsDFS(root, "", result);
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
            result.add(out + "->" + root.val);
        }

        binaryTreePathsDFS(root.left, out + root.val + "->", result);
        binaryTreePathsDFS(root.right, out + root.val + "->", result);
    }
}

