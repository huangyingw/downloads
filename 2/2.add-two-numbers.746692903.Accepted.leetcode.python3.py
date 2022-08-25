class Solution:
    def addTwoNumbers(self, l1, l2):
        StartAns = Answer = ListNode(0)
        carry = 0
        while l1 and l2:
            carry, sumval = divmod(l1.val + l2.val + carry, 10)
            Answer.next = ListNode(sumval)
            l1 = l1.next
            l2 = l2.next
            Answer = Answer.next
        tmplist = l1 or l2
        while tmplist:
            carry, sumval = divmod(tmplist.val + carry, 10)
            Answer.next = ListNode(sumval)
            tmplist = tmplist.next
            Answer = Answer.next
        if carry != 0:
            Answer.next = ListNode(carry)
        return StartAns.next

