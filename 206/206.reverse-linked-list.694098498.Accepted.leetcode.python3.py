class Solution(object):
    def reverseList(self, head):
        reversed = None
        while head:
            nex = head.next
            head.next = reversed
            reversed = head
            head = nex
        return reversed

