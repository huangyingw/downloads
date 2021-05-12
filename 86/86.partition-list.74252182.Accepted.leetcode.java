public class Solution
{
    public ListNode partition(ListNode head, int x)
    {
        if (head == null)
        {
            return null;
        }

        ListNode leftDummy = new ListNode(-1);
        ListNode rightDummy = new ListNode(-1);
        ListNode left = leftDummy, right = rightDummy;
        
        while(head != null)
        {
            if(head.val < x)
            {
                left.next = head;
                left = head;
            }
            else
            {
                right.next = head;
                right = head;
            }
            
            head = head.next;
        }

        right.next = null;
        left.next = rightDummy.next;
        return leftDummy.next;
    }
}

