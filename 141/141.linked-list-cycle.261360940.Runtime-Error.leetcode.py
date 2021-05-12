class Solution(object):
    def hasCycle(self, head):
        if not fast:
            return False
        fast, slow = head.next, head
        while fast and fast.next:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next
        return False

