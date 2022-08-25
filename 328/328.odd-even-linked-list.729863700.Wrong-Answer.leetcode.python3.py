class Solution(object):
    def oddEvenList(self, head):
        even_head = even = ListNode(None)
        odd_head = odd = ListNode(None)
        while head and head.next:
            odd.next = head
            print("odd --> %s" % odd.val)
            odd = odd.next
            even.next = head.next
            print("even --> %s" % even.val)
            even = even.next
            head = head.next.next
        odd.next = even_head.next
        return odd_head.next

