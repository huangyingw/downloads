public class Solution {
    public ListNode partition(ListNode head, int x) {
      ListNode left_dummy = new ListNode(-1);
      ListNode right_dummy = new ListNode(-1);
      ListNode left_cur = left_dummy;
      ListNode right_cur = right_dummy;

      for (ListNode cur = head; cur != null; cur = cur.next) {
        if (cur.val < x) {
          left_cur.next = cur;
          left_cur = cur;
        }
        else {
          right_cur.next = cur;
          right_cur = cur;
        }
      }

      left_cur.next = right_dummy.next;
      right_cur.next = null;
      return left_dummy.next;
    }
  }

