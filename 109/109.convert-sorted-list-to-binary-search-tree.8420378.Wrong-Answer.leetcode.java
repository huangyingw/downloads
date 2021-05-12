  public class Solution {

    public TreeNode sortedListToBST(ListNode head) {
      if (head == null) {
        return null;
      }

      int len = getLength(head);
      return sortedListToBST(head, 0, len - 1);
    }

    public int getLength(ListNode head) {
      int len = 0;
      ListNode p = head;

      while (p != null) {
        len++;
        p = p.next;
      }

      return len;
    }

    public TreeNode sortedListToBST(ListNode head, int start, int end) {
      if (start > end) {
        return null;
      }

      int mid = (start + end) / 2;
      TreeNode left = sortedListToBST(head, start, mid - 1);
      TreeNode root = new TreeNode(head.val);
      head = head.next;
      TreeNode right = sortedListToBST(head, mid + 1, end);
      root.left = left;
      root.right = right;
      return root;
    }
  }

