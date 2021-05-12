public class BSTIterator
{
    Stack<TreeNode> stack;

    public BSTIterator(TreeNode root)
    {
        stack = new Stack<TreeNode>();

        while (root != null)
        {
            stack.push(root);
            root = root.left;
        }
    }

    public boolean hasNext()
    {
        return !stack.isEmpty();
    }

    public int next()
    {
        TreeNode root = stack.pop();
        int result = root.val;

        if (root.right != null)
        {
            root = root.right;

            while (root != null)
            {
                stack.push(root);
                root = root.left;
            }
        }

        return result;
    }
}

