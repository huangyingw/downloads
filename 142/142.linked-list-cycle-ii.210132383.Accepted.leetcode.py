class Solution(object):
    def detectCycle(self, head):
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                while fast != head:
                    fast = fast.next
                    head = head.next
                return fast
        return None

