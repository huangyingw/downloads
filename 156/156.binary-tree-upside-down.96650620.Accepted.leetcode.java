public class Solution
{
    public TreeNode upsideDownBinaryTree(TreeNode root)
    {
        TreeNode navNode = root, parentNode = null, leftNode = null, rightNode = null;

        while (navNode != null)
        {
            leftNode = navNode.left;
            navNode.left = rightNode;
            rightNode = navNode.right;
            navNode.right = parentNode;
            parentNode = navNode;
            navNode = leftNode;
        }

        return parentNode;
    }
}
