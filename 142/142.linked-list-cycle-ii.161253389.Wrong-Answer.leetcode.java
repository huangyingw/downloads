public class Solution
{
    public ListNode detectCycle(ListNode head)
    {
        ListNode fast = head;
        ListNode slow = head;

        while (fast != null && fast.next != null && fast != slow)
        {
            fast = fast.next.next;
            slow = slow.next;
        }

        while (fast != null && fast != head)
        {
            fast = fast.next;
            head = head.next;
        }

        return fast;
    }
}

