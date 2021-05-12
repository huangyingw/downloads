class Solution(object):
    def oddEvenList(self, head):
        odd = head
        if head is None:
            return None
        if head.next is None:
            return head
        even_head = even = head.next
        while odd.next is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head

