class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = cur = ListNode(0)
        nodes_sum = 0
        while l1 or l2 or nodes_sum:
            if l1:
                nodes_sum += l1.val
                l1 = l1.next
            if l2:
                nodes_sum += l2.val
                l2 = l2.next
            cur.next = ListNode(nodes_sum % 10)
            cur = cur.next
            nodes_sum //= 10
        return res.next

