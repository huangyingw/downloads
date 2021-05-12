public class Solution
{
    public ListNode insertionSortList(ListNode head)
    {
        if (head == null)
        {
            return null;
        }

        ListNode dummy = new ListNode(0);
        ListNode pre = dummy;
        ListNode cur = head;
        ListNode nextNode = null;

        while (cur != null)
        {
            pre = dummy;

            while (pre.next != null && pre.next.val < cur.val)
            {
                pre = pre.next;
            }
        }

        return dummy.next;
    }
}

