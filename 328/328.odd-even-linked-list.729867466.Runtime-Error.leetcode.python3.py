class Solution(object):
    def oddEvenList(self, head):
        even_head = even = ListNode(None)
        odd_head = odd = ListNode(None)
        while head:
            odd.next = head
            odd = odd.next
            print("odd --> %s" % odd.val)
            even.next = head.next
            even = even.next
            print("even --> %s" % even.val)
            if head.next:
                head = head.next.next
            print("head --> %s" % head.val)
        odd.next = even_head.next
        return odd_head.next

