class Solution(object):
    def oddEvenList(self, head):
        even_head = even = ListNode(None)
        odd_head = odd = ListNode(None)
        while head and head.next:
            odd.next = head
            odd = odd.next
            print("odd --> %s" % odd.val)
            even.next = head.next
            even = even.next
            print("even --> %s" % even.val)
            head = head.next.next
        odd.next = even_head.next
        return odd_head.next

