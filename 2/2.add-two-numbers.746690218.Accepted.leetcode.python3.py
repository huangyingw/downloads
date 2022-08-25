class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        res = l1
        while l1 or l2:
            l1.val += l2.val + carry if l2 else carry
            carry = l1.val // 10
            l1.val %= 10
            if l2:
                l2 = l2.next
            if l1.next:
                l1 = l1.next
            elif carry or l2:
                l1.next = ListNode(0)
                l1 = l1.next
            else:
                break
        return res

