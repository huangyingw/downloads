class Solution(object):
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        new_start = head.next.next
        head, head.next = head.next, head
        head.next.next = self.swapPairs(new_start)
        return head

