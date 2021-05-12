public class Solution
{
    private ListNode findMiddle(ListNode head)
    {
        ListNode slow = head, fast = head.next;

        while (fast != null && fast.next != null)
        {
            fast = fast.next.next;
            slow = slow.next;
        }

        return slow;
    }

    private ListNode merge(ListNode head1, ListNode head2)
    {
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;

        while (head1 != null || head2 != null)
        {
            if (head2 == null || (head1 != null && head1.val < head2.val))
            {
                tail.next = head1;
                head1 = head1.next;
            }
            else
            {
                tail.next = head2;
                head2 = head2.next;
            }

            tail = tail.next;
        }

        return dummy.next;
    }

    public ListNode sortList(ListNode head)
    {
        ListNode mid = findMiddle(head);
        ListNode right = sortList(mid.next);
        mid.next = null;
        ListNode left = sortList(head);
        return merge(left, right);
    }
}

