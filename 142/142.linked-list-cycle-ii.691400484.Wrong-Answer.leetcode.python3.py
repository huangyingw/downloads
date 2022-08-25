class Solution(object):
    def detectCycle(self, head):
        fast = head
        slow = head
        while fast and fast.next and fast != slow:
            fast = fast.next.next
            slow = slow.next
        while fast != head:
            fast = fast.next
            head = head.next
        return fast

