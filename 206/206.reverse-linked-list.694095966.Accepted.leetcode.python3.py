class Solution(object):
    def reverseList(self, head):
        if not head:
            return None
        prev, curr = None, head
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        return prev

