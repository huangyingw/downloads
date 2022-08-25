class Solution(object):
    def detectCycle(self, head):
        if not head or not head.next:
            return None
        q1 = head
        q2 = head.next
        while q1 != q2:
            if not q2 or not q2.next:
                return None
            q1 = q1.next
            q2 = q2.next.next
        res = head
        q1 = q1.next
        while res != q1:
            res = res.next
            q1 = q1.next
        return res

