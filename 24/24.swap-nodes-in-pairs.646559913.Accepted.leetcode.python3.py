class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        prev, p = dummy, head
        while p and p.next:
            q, r = p.next, p.next.next
            prev.next = q
            q.next = p
            p.next = r
            prev = p
            p = r
        return dummy.next

