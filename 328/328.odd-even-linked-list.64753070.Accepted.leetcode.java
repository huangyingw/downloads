  public class Solution
  {
    public ListNode oddEvenList(ListNode head)
    {
      if (head == null)
      {
        return head;
      }

      ListNode p = head, q = head;

      while (q != null)
      {
        q = q.next;

        if (q == null || q.next == null)
        {
          break;
        }

        ListNode next_p = p.next, next_q = q.next;
        q.next = next_q.next;
        p.next = next_q;
        next_q.next = next_p;
        p = p.next;
      }

      return head;
    }
  }

