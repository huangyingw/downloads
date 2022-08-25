class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = current = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, value = divmod(carry, 10)
            current.next = ListNode(value)
            current = current.next
        return dummy.next

