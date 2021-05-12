public class Solution
{
    private ListNode current;

    public TreeNode sortedListToBST(ListNode head)
    {
        current = head;
        int size = 0;

        while (head != null)
        {
            size++;
            head = head.next;
        }

        return dfs(0, size - 1);
    }

    public TreeNode dfs(int start, int end)
    {
        if (start > end)
        {
            return null;
        }

        int mid = (start + end) / 2;
        TreeNode left = dfs(start, mid - 1);
        TreeNode root = new TreeNode(current.val);
        current = current.next;
        TreeNode right = dfs(mid + 1, end);
        root.left = left;
        root.right = right;
        return root;
    }
}

