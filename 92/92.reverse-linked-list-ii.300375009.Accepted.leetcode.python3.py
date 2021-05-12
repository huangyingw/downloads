class Solution(object):
    def reverseBetween(self, head, m, n):
        pseudo = ListNode(None)
        pseudo.next = head
        node = pseudo
        n -= m
        while m > 1:
            node = node.next
            m -= 1
        reversed_head = None
        next_reverse = node.next
        while n >= 0:
            tail = next_reverse.next
            next_reverse.next = reversed_head
            reversed_head = next_reverse
            next_reverse = tail
            n -= 1
        node.next.next = tail
        node.next = reversed_head
        return pseudo.next

