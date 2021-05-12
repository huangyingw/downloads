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
            nextNode = cur.next;
            cur.next = pre.next;
            pre.next = cur;
            cur = nextNode;
        }

        return dummy.next;
    }
}

