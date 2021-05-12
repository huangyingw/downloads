class Solution(object):
    def reorderList(self, head):
        if not head:
            return None
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev, node = None, slow
        while node:
            prev, node.next, node = node, prev, node.next
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

