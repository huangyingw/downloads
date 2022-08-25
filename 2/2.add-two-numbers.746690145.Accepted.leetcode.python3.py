class Solution(object):
    def addTwoNumbers(self, l1, l2):
        res = ListNode(0)
        cur = res
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            summ = carry + x + y
            carry = summ // 10
            cur.next = ListNode(summ % 10)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            cur.next = ListNode(carry)
        return res.next

