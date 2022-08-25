class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(-1)
        dummy.next = head
        first, second = dummy, dummy
        for i in range(n):
            first = first.next
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next

