public class Solution {
    public ListNode rotateRight(ListNode head, int n) {
      if (head == null || n == 0) {
        return head;
      }

      int len = 1;
      ListNode p = head;

      while (p.next != null) {
        len++;
        p = p.next;
      }

      n = len - n % len;
      p.next = head;

      for (int step = 0; step < n; step++) {
        p = p.next;
      }

      head = p.next;
      p.next = null;
      return head;
    }
  }

