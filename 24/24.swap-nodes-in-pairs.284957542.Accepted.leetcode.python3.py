class Solution(object):
    def swapPairs(self, head: ListNode) -> ListNode:
        newHead = ListNode(0)
        newHead.next = head
        cur = newHead
        while cur.next and cur.next.next:
            a = cur.next
            b = cur.next.next
            cur.next = b
            a.next = b.next
            b.next = a
            cur = a
        return newHead.next

