class Solution(object):
    def sortList(self, head):
        if not head:
            return head
        middleNode = self.findMiddleNode(head)
        right = middleNode.next
        middleNode.next = None
        return self.mergeList(self.sortList(head), self.sortList(right))

    def findMiddleNode(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def mergeList(self, left, right):
        dummy = ListNode(None)
        node = dummy
        while left and right:
            if left.val < right.val:
                node.next = left
                left = left.next
            else:
                node.next = right
                right = right.next
            node = node.next
        node.next = left or right
        return dummy.next

