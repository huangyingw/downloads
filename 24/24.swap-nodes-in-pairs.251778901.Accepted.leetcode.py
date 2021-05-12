class Solution:
    def swapPairs(self, head):
        dummy = p = ListNode(0)
        dummy.next = head
        while head and head.next:
            curr = head.next
            head.next, curr.next = curr.next, head
            p.next = curr
            p = head
            head = head.next
        return dummy.next

