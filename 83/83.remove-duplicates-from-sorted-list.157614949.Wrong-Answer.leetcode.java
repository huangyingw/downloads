public class Solution
{
    public ListNode deleteDuplicates(ListNode head)
    {
        ListNode current = head;

        while (current != null)
        {
            if (current.next != null && current.val == current.next.val)
            {
                current.next = current.next.next;
            }

            current = current.next;
        }

        return head;
    }
}

