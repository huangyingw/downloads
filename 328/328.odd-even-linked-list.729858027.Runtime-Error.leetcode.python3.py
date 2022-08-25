class Solution(object):
    def oddEvenList(self, head):
        odd, even = head, head.next
        evenHead = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head

