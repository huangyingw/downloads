class Solution(object):
    def reverseList(self, head):
        reversed = None
        while head:
            next = head.next
            head.next = reversed
            reversed = head
            head = next
        return reversed

