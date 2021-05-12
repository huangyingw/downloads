public class BSTIterator
{
    private Stack<TreeNode> stack = new Stack<>();
    private TreeNode top;
    public BSTIterator(TreeNode root)
    {
        top = root;
    }
    public boolean hasNext()
    {
        return (!stack.isEmpty() || top != null);
    }
    public int next()
    {
        while (top != null)
        {
            stack.push(top);
            top = top.left;
        }

        top = stack.pop();
        int result = top.val;
        top = top.right;
        return result;
    }
}
