class Solution(object):
    def reverseList(self, head):
        if not head:
            return head
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

