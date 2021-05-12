public class Solution
{
    public ListNode detectCycle(ListNode head)
    {
        ListNode fast = head;
        ListNode slow = head;

        while (fast != null && fast.next != null && fast != slow)
        {
            fast = fast.next.next;
            System.out.printf("fast --> %s\n", fast.val);
            slow = slow.next;
        }

        while (fast != null && fast != head)
        {
            fast = fast.next;
            System.out.printf("fast --> %s\n", fast.val);
            head = head.next;
        }

        return fast;
    }
}

