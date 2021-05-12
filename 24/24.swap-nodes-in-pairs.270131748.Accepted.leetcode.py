class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        while prev and prev.next and prev.next.next:
            current = prev.next.next
            prev.next.next = current.next
            current.next = prev.next
            prev.next = current
            prev = prev.next.next
        return dummy.next

