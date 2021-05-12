class Solution(object):
    def hasCycle(self, head):
        if not head:
            return False
        slow, fast = head, head.next
        while slow != fast and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return False

