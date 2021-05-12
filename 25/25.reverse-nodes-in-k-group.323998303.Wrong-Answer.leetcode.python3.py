class Solution(object):
    def reverseKGroup(self, head, k):
        if k < 2:
            return head
        node = head
        for _ in range(k):
            if not node:
                return head
            node = node.next
        prev = None
        for _ in range(k):
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        prev = self.reverseKGroup(node, k)
        return prev

