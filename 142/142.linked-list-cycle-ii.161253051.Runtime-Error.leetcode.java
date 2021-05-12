public class Solution
{
    public ListNode detectCycle(ListNode head)
    {
        ListNode fast = head;
        ListNode slow = head;

        do
        {
            if (fast.next == null)
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

