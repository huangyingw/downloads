public class Solution
{
    public ListNode mergeTwoLists(ListNode l1, ListNode l2)
    {
        ListNode head = new ListNode(-1);
        ListNode nav = head;

        while (l1 != null || l2 != null)
        {
            if (l2 == null || l1 != null && l1.val < l2.val)
            {
                nav.next = l1;
                l1 = l1.next;
            }
            else
            {
                nav.next = l2;
                l2 = l2.next;
            }

            nav = nav.next;
        }

        return head.next;
    }
}

