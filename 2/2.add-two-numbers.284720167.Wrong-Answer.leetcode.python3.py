class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = ListNode(-1)
        current = head
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            current.next = ListNode(carry % 10)
            current = current.next
            carry /= 10
        return head.next

