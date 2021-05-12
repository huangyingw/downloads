class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow:
            temp = slow
            slow = slow.next
            temp.next = prev
            prev = temp
        start = head
        while prev.next:
            start.next, start = prev, start.next
            prev.next, prev = start, prev.next

