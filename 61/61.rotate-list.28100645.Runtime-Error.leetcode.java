/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if(head == null || head.next == null)
            return head;
        ListNode cur = head;
        ListNode pre = head;
        for(int i = 0;i<k;i++)
        {
            cur = cur.next;
        }
        while(cur != null && cur.next != null)
        {
            pre = pre.next;
            cur = cur.next;
        }
        cur.next = head;
        head = pre.next;
        pre.next = null;
        return head;
    }
}
