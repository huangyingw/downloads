class Solution(object):
    def removeNthFromEnd(self, head, n):
        first, second = head, head
        for i in range(n):
            first = first.next
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return head

