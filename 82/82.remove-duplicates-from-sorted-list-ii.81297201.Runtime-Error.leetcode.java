public class Solution
{
    public ListNode deleteDuplicates(ListNode head)
    {
        if(head == null)
        {
            return null;
        }
        
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        head = dummy;
        
        while(head.next != null)
        {
            if(head.next.val == head.next.next.val)
            {
                int val = head.next.val;
                while(val == head.next.val)
                {
                    head.next = head.next.next;
                }
            }
            else
            {
                head = head.next;
            }
        }
        
        return dummy.next;
    }
}
