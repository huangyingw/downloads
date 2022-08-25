class Solution(object):
    def reverseList(self, head):
        prev = None
        while head:
            nex = head.next
            head.next = prev
            prev = head
            head = nex
        return prev

