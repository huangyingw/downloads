class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        prev, p = dummy, head
        while p != None and p.next != None:
            q, r = p.next, p.next.next
            prev.next = q
            q.next = p
            p.next = r
            prev = p
            p = r
        return dummy.next

