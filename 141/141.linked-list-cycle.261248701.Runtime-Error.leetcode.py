class Solution(object):
    def hasCycle(self, head):
        if not head:
            return False
        slow = fast = head
        while True:
            if not fast:
                return False
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

