public class Solution
{
    public ListNode reverseBetween(ListNode head, int m, int n)
    {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prevM = dummy;
        ListNode prev = null;

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
                ListNode temp = head.next;
                head.next = prev;
                prev = head;
                head = temp;
            }
        }

        prevM.next.next = head;
        prevM.next = prev;
        return dummy.next;
    }
}

