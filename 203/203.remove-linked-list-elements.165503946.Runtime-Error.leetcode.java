public class Solution
{
    public ListNode removeElements(ListNode head, int val)
    {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode p = dummy;

        while (p.next != null)
        {
            if (p.next.val == val)
            {
                System.out.printf("p.next.next --> %s\n", p.next.next != null ? p.next.next.val : "null");
                p.next = p.next.next;
                System.out.printf("p.next --> %s\n", p.next != null ? p.next.val : "null");
            }

            p = p.next;
            System.out.printf("p --> %s\n", p != null ? p.val : "null");
        }

        return dummy.next;
    }
}

