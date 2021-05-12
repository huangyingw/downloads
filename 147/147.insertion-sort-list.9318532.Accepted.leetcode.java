  public class Solution {
    public ListNode insertionSortList(ListNode head) {
      if (head == null) {
        return null;
      }

      ListNode helper = new ListNode(0);
      ListNode pre = helper;
      ListNode cur = head;
      ListNode next = null;

      while (cur != null) {
        pre = helper;

        while (pre.next != null && pre.next.val < cur.val) {
          pre = pre.next;
        }

        next = cur.next;
        cur.next = pre.next;
        pre.next = cur;
        cur = next;
      }

      return helper.next;
    }
  }

