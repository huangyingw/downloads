class Solution(object):
    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next and fast != slow:
            slow = slow.next
            fast = fast.next.next
        if not fast or not fast.next:
            return None
        while head != fast:
            head = head.next
            fast = fast.next
        return fast

