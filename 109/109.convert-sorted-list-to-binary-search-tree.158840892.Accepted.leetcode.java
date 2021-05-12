public class Solution
{
    private ListNode current;
    private TreeNode sortedListToBST(int begin, int end)
    {
        if (begin > end)
        {
            return null;
        }

        TreeNode root = new TreeNode(0);
        int mid = (begin + end) / 2;
        root.left = sortedListToBST(begin, mid - 1);
        root.val = current.val;
        current = current.next;
        root.right = sortedListToBST(mid + 1, end);
        return root;
    }

    public TreeNode sortedListToBST(ListNode head)
    {
        current = head;
        int len = 0;

        while (head != null)
        {
            len++;
            head = head.next;
        }

        return sortedListToBST(0, len - 1);
    }
}

