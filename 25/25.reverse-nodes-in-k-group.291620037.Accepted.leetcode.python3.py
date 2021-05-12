class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1 or not head:
            return head
        count = 0
        dummyHead = ListNode(0)
        dummyHead.next = head
        begin = dummyHead
        while head:
            count += 1
            # If (head - begin) == k
            if count % k == 0:
                begin = self.reverseList(begin, head.next)
                head = begin.next
            else:
                head = head.next
        return dummyHead.next

    def reverseList(self, begin, end):
        cur = begin.next
        prev = begin
        first = cur
        while cur != end:
            cur.next, prev, cur = prev, cur, cur.next
        begin.next = prev
        first.next = cur
        return first

