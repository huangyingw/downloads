class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        nextHead = head.next.next
        newHead = head.next
        head.next.next = head
        head.next = self.swapPairs(nextHead)
        return newHead

