public class Solution
{
    public ListNode detectCycle(ListNode head)
    {
        if (head == null)
        {
            return null;
        }

        ListNode fast = head;
        ListNode slow = head;

        do
        {
            if (fast == null || fast.next == null)
            {
                return null;
            }

            fast = fast.next.next;
            slow = slow.next;
        }
        while (fast != slow);

        slow = head;

        while (fast != slow)
        {
            fast = fast.next;
            slow = slow.next;
        }

        return fast;
    }
}

