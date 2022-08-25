class Solution(object):
    def detectCycle(self, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        if not slow or not fast:
            return None
        while fast != head:
            fast = fast.next
            head = head.next
        return fast

