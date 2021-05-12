class Solution(object):
    def reverseKGroup(self, head, k):
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        count = 0

        while head:
            count += 1

            if count % k == 0:
                pre = self.reverse(pre, head.next)
                head = pre.next
            else:
                head = head.next
        return dummy.next

    def reverse(self, pre, next):
        last = pre.next
        cur = last.next

        while cur != next:
            last.next = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = last.next
        return last

