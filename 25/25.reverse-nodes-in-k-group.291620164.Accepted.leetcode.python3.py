class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        newhead = head
        for i in range(k):
            if newhead == None:
                return head
            newhead = newhead.next
        connect = cur = head
        prev = None
        for i in range(k):
            cur.next, cur, prev = prev, cur.next, cur
        connect.next = self.reverseKGroup(newhead, k)
        return prev

