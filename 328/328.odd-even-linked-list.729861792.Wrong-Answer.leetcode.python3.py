class Solution(object):
    def oddEvenList(self, head):
        even_head = even = ListNode(None)
        odd_head = odd = ListNode(None)
        while head and head.next:
            odd.next = head
            odd = odd.next
            even.next = head.next
            even = even.next
            head = head.next.next
        odd.next = even_head.next
        return odd_head.next

