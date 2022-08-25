class Solution(object):
    def reverseList(self, head):
        if not head:
            return None
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

