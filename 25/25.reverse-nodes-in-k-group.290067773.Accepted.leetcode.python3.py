class Solution:
    def reverseKGroup(self, head, k):
        dummy = jump = ListNode(0)
        dummy.next = head
        l, r = head, head
        while True:
            count = 0
            while r and count < k:
                count += 1
                r = r.next
            if count == k:
                curr, prev = l, r
                for _ in range(k):
                    curr.next, prev, curr = prev, curr, curr.next
                jump.next, jump, l = prev, l, r
            else:
                return dummy.next

