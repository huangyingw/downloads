public class Solution
{
    public ListNode reverseBetween(ListNode head, int m, int n)
    {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prevM = dummy;
        ListNode prev = null;
        ListNode temp = null;

        for (int i = 1; i <= n; i++)
        {
            if (i < m)
            {
                prevM = prevM.next;
            }
            else if (i == m)
            {
                prev = prevM.next;
                head = prev.next;
            }
            else
            {
                temp = head.next;
                head.next = prev;
                prev = head;
                head = temp;
            }
        }

        prevM.next.next = temp;
        prevM.next = prev;
        return dummy.next;
    }
}

