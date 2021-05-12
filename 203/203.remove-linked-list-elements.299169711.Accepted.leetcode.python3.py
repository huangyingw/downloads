class Solution(object):
    def removeElements(self, head, val):
        dummy = prev = ListNode(None)
        dummy.next = head
        while head:
            if head.val == val:
                prev.next, head.next, head = head.next, None, head.next
            else:
                prev, head = head, head.next
        return dummy.next

