class Solution(object):
    def hasCycle(self, head):
        if not head:
            return False
        slow = fast = head
        while True:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

