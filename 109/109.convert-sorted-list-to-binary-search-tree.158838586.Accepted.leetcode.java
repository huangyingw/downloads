public class Solution
{
    private ListNode current;

    private int getListLength(ListNode head)
    {
        int size = 0;

        while (head != null)
        {
            size++;
            head = head.next;
        }

        return size;
    }

    public TreeNode sortedListToBST(ListNode head)
    {
        current = head;
        return sortedListToBSTHelper(0, getListLength(head) - 1);
    }

    public TreeNode sortedListToBSTHelper(int start, int end)
    {
        if (start > end)
        {
            return null;
        }

        int mid = (start + end) / 2;
        TreeNode left = sortedListToBSTHelper(start, mid - 1);
        TreeNode root = new TreeNode(current.val);
        current = current.next;
        TreeNode right = sortedListToBSTHelper(mid + 1, end);
        root.left = left;
        root.right = right;
        return root;
    }
}

